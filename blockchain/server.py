import time
import threading
import requests
from fastapi import FastAPI
from blockchain.ethereum.contracts import get_lock_contract

app = FastAPI(title="Blockchain Service")

DJANGO_URL = "http://backend:8000/blockchain-data/"

# ==============================
# Helpers
# ==============================
def get_lock():
    return get_lock_contract()

# ==============================
# Event handling
# ==============================
def handle_event(event):
    payload = {
        "tx_hash": event["transactionHash"].hex(),
        "contract_address": event["address"],
    }

    try:
        res = requests.post(DJANGO_URL, json=payload, timeout=5)
        res.raise_for_status()
        print("Event sent to Django:", payload)
    except Exception as e:
        print("Failed to send event:", e)

# ==============================
# Event listener
# ==============================
def event_listener():
    lock = get_lock()
    last_block = lock.web3.eth.block_number

    while True:
        try:
            current_block = lock.web3.eth.block_number

            if current_block > last_block:
                events = lock.contract.events.Withdrawal().get_logs(
                    fromBlock=last_block + 1,
                    toBlock=current_block
                )

                for event in events:
                    handle_event(event)

                last_block = current_block

        except Exception as e:
            print("Event listener error:", e)

        time.sleep(2)

# ==============================
# FastAPI lifecycle
# ==============================
@app.on_event("startup")
def start_event_listener():
    threading.Thread(target=event_listener, daemon=True).start()

# ==============================
# API endpoints
# ==============================
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/health/blockchain")
def blockchain_health():
    lock = get_lock()
    return {
        "owner": lock.owner(),
        "unlock_time": lock.unlock_time()
    }

@app.post("/contracts/lock/withdraw")
def withdraw_lock():
    lock = get_lock()
    receipt = lock.withdraw()
    return {"tx_hash": receipt.transactionHash.hex()}




