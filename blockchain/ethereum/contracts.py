# ethereum/contracts.py

import os
import json
from web3 import Web3
from .client import EthereumClient

# ==============================
# Paths and ABI
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCK_JSON_PATH = os.path.join(BASE_DIR, "hardhat/artifacts/contracts/Lock.sol/Lock.json")
LOCK_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"  # Update if deployed differently

with open(LOCK_JSON_PATH, "r") as f:
    LOCK_ABI = json.load(f)["abi"]

# ==============================
# LockContract Wrapper
# ==============================
class LockContract:
    def __init__(self, web3: Web3, signer: str, address=LOCK_ADDRESS, abi=LOCK_ABI):
        self.web3 = web3
        self.signer = signer
        self.address = address
        self.abi = abi
        self.contract = web3.eth.contract(address=address, abi=abi)

    def owner(self):
        """Read-only call to owner()"""
        return self.contract.functions.owner().call()

    def unlock_time(self):
        """Read-only call to unlockTime()"""
        return self.contract.functions.unlockTime().call()

    def withdraw(self):
        """Build, sign, and send withdraw transaction"""
        tx = self.contract.functions.withdraw().build_transaction({
            "from": self.signer,
            "nonce": self.web3.eth.get_transaction_count(self.signer),
            "gas": 200000,
            "gasPrice": self.web3.to_wei("20", "gwei"),
            "chainId": 31337,
        })

        private_key = os.getenv("PRIVATE_KEY")
        if not private_key:
            raise ValueError("Set PRIVATE_KEY env variable for signing transaction")

        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key=private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for receipt
        receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        if receipt.status == 1:
            print(f"Transaction successful: {tx_hash.hex()}")
        else:
            print(f"Transaction failed: {tx_hash.hex()}")
        return receipt

# ==============================
# Helper to get LockContract instance
# ==============================
def get_lock_contract(rpc_url="http://hardhat-service:8545"):
    """
    Connects to the Ethereum node and returns LockContract instance
    """
    eth_client = EthereumClient(rpc_url=rpc_url)
    if not eth_client.is_connected():
        raise ConnectionError(f"Cannot connect to Ethereum node at {rpc_url}")
    signer = eth_client.get_signer()
    return LockContract(web3=eth_client.web3, signer=signer)
