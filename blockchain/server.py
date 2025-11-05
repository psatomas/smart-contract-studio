# blockchain/server.py

from fastapi import FastAPI
import requests
import time
from ethereum.contracts import  signer, lock  # your Hardhat EVM contract setup

app = FastAPI(title="Blockchain Service")

# Django backend URL
DJANGO_URL = "http://backend:8000/blockchain-data/"

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/contracts/lock/withdraw")
def withdraw_lock_contract():
    try:
        # Call withdraw on Solidity contract
        tx = lock.withdraw()  # already returns ContractTransactionResponse
        tx_hash = tx.hash.hex()
        value = 0  # optionally fetch value if your contract stores ETH
        contract_address = lock.address

        # Send event to Django
        send_to_backend(tx_hash, value, contract_address)

        return {"status": "success", "tx_hash": tx_hash, "contract_address": contract_address}

    except Exception as e:
        return {"status": "error", "message": str(e)}


def send_to_backend(tx_hash: str, value: float, contract_address: str):
    payload = {
        "tx_hash": tx_hash,
        "value": value,
        "contract_address": contract_address
    }

    retries = 5
    for i in range(retries):
        try:
            response = requests.post(DJANGO_URL, json=payload)
            response.raise_for_status()
            print("Sent to Django:", response.json())
            return
        except requests.RequestException as e:
            print(f"Attempt {i+1}/{retries} failed: {e}")
            time.sleep(2)

    print("Failed to reach Django after 5 attempts")

