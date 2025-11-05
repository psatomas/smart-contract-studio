from fastapi import FastAPI
import requests
import time
from ethereum.contracts import lock  # your Hardhat EVM contract setup
import threading

app = FastAPI(title="Blockchain Service")

DJANGO_URL = "http://backend:8000/blockchain-data/"

@app.get("/health")
def health_check():
    return {"status": "ok"}

# ... other endpoints here ...

# Event listener thread
def handle_event(event):
    payload = {
        "tx_hash": event["transactionHash"].hex(),
        "contract_address": event["address"],
        "args": dict(event["args"])
    }
    try:
        res = requests.post(DJANGO_URL, json=payload)
        print("Event sent to Django:", res.status_code, res.text)
    except Exception as e:
        print("Failed sending event:", e)

def event_listener():
    last_block = lock.web3.eth.block_number  # start from current block

    while True:
        current_block = lock.web3.eth.block_number
        if current_block > last_block:
            # Fetch Withdrawal events from last_block+1 to current_block
            events = lock.contract.events.Withdrawal.get_logs(
                from_block=last_block + 1,
                to_block=current_block
            )
            for event in events:
                handle_event(event)
            last_block = current_block
        time.sleep(2)  # poll every 2 seconds

listener_thread = threading.Thread(target=event_listener, daemon=True)
listener_thread.start()
