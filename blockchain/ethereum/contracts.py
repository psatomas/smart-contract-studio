
import os
import json
from .client import EthereumClient

# Dummy client (replace with actual Hardhat connection later)
eth_client = EthereumClient()

# Load deployed Lock contract info
LOCK_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"  # example from deploy

# Make path absolute relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # blockchain/ethereum
ABI_PATH = os.path.join(BASE_DIR, "hardhat/artifacts/contracts/Lock.sol/Lock.json")

with open(ABI_PATH, "r") as f:
    LOCK_ABI = json.load(f)["abi"]

# Placeholder signer
class Signer:
    def send_transaction(self, tx):
        print("Sending transaction:", tx)
        return {"hash": "0xDEADBEEF"}

signer = Signer()

# Minimal contract wrapper
class LockContract:
    def __init__(self, address, abi):
        self.address = address
        self.abi = abi

    def withdraw(self):
        print("Calling withdraw on Lock contract")
        return type("TxResponse", (), {"hash": b"\xde\xad\xbe\xef"})()

lock = LockContract(LOCK_ADDRESS, LOCK_ABI)