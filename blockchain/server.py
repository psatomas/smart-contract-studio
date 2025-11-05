# blockchain/server.py
import time
import threading
import requests
from fastapi import FastAPI
from ethereum.contracts import lock  # your Hardhat Lock contract

app = FastAPI(title="Blockchain Service")

DJANGO_URL = "http://127.0.0.1:8000/blockchain-data/"

# ---------------------------
# Event handling
# ---------------------------
def handle_event(event):
    payload = {
        "tx_hash": event["transactionHash"].hex(),
        "contract_address": event["address"],
        "amount": event["args"]["amount"],
        "timestamp": event["args"]["when"]
    }
    try:
        res = requests.post(DJANGO_URL, json=payload)
        res.raise_for_status()
        print("Event sent to Django successfully:", payload)
    except Exception as e:
        print("Failed sending event to Django:", e)


# ---------------------------
# Event listener thread
# ---------------------------
def event_listener():
    last_block = lock.web3.eth.block_number

    while True:
        current_block = lock.web3.eth.block_number
        if current_block > last_block:
            try:
                events = lock.contract.events.Withdrawal().get_logs(
                    fromBlock=last_block + 1,
                    toBlock=current_block
                )
                for event in events:
                    handle_event(event)
                last_block = current_block
            except Exception as e:
                print("Error fetching events:", e)

        time.sleep(2)


listener_thread = threading.Thread(target=event_listener, daemon=True)
listener_thread.start()


# ---------------------------
# FastAPI endpoints
# ---------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/contracts/lock/withdraw")
def withdraw_lock():
    try:
        # Trigger withdraw and get the tx object
        tx = lock.withdraw()  # Your lock object handles signing & sending internally
        # Return the real transaction hash
        tx_hash = getattr(tx, "hash", None)
        if tx_hash:
            return {"status": "success", "tx_hash": tx_hash.hex()}
        else:
            return {"status": "success", "tx": str(tx)}
    except Exception as e:
        return {"status": "error", "message": str(e)}



