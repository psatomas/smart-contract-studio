from fastapi import FastAPI
from ethereum import client, contracts
import requests
import time

app = FastAPI(title="Blockchain Service")

# URL for Django backend inside Docker network
DJANGO_URL = "http://backend:9000/blockchain-data/"

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/contracts/dummy")
def get_dummy_contract():
    contract_address = contracts.deploy_dummy_contract()
    send_to_backend(tx_hash="dummy_tx_hash", value=123.45, contract_address=contract_address)
    return {"address": contract_address}

@app.get("/trigger")
def trigger_backend_call():
    # Manually send dummy data to Django
    send_to_backend(tx_hash="0x123abc", value=42.0, contract_address="0xDUMMY")
    return {"status": "sent"}

def send_to_backend(tx_hash: str, value: float, contract_address: str):
    payload = {
        "tx_hash": tx_hash,
        "value": value,
        "contract_address": contract_address
    }

    # Retry logic in case backend isn't up yet
    retries = 5
    for i in range(retries):
        try:
            response = requests.post(DJANGO_URL, json=payload)
            response.raise_for_status()
            print("Sent to backend:", response.json())
            return
        except requests.RequestException as e:
            print(f"Attempt {i+1}/{retries} failed: {e}")
            time.sleep(2)
    print("Failed to reach backend after 5 attempts")