import os
import json
from web3 import Web3
from .client import EthereumClient

# ==============================
# Paths and ABI
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOCK_JSON_PATH = os.path.join(
    BASE_DIR,
    "hardhat/artifacts/contracts/Lock.sol/Lock.json"
)

LOCK_ADDRESS = os.getenv(
    "LOCK_ADDRESS",
    "0x5FbDB2315678afecb367f032d93F642f64180aa3"
)

with open(LOCK_JSON_PATH, "r") as f:
    LOCK_ABI = json.load(f)["abi"]

# ==============================
# LockContract wrapper
# ==============================
class LockContract:
    def __init__(self, web3: Web3, signer: str):
        self.web3 = web3
        self.signer = signer
        self.contract = web3.eth.contract(
            address=LOCK_ADDRESS,
            abi=LOCK_ABI
        )

    def owner(self):
        return self.contract.functions.owner().call()

    def unlock_time(self):
        return self.contract.functions.unlockTime().call()

    def withdraw(self):
        tx = self.contract.functions.withdraw().build_transaction({
            "from": self.signer,
            "nonce": self.web3.eth.get_transaction_count(self.signer),
            "gas": 200000,
            "gasPrice": self.web3.to_wei("20", "gwei"),
            "chainId": 31337,
        })

        private_key = os.getenv("PRIVATE_KEY")
        if not private_key:
            raise RuntimeError("PRIVATE_KEY not set")

        signed = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(tx_hash)

# ==============================
# Lazy singleton
# ==============================
_lock = None

def get_lock_contract():
    global _lock
    if _lock is None:
        client = EthereumClient(
            rpc_url=os.getenv("ETH_RPC_URL", "http://127.0.0.1:8545")
        )
        if not client.is_connected():
            raise ConnectionError("Cannot connect to Ethereum node")

        _lock = LockContract(
            web3=client.web3,
            signer=client.get_signer()
        )
    return _lock
