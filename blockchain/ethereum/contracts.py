from web3 import Web3
from .client import EthereumClient
import json, os

eth_client = EthereumClient()
web3 = eth_client.web3

LOCK_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ABI_PATH = os.path.join(BASE_DIR, "hardhat/artifacts/contracts/Lock.sol/Lock.json")

with open(ABI_PATH, "r") as f:
    LOCK_ABI = json.load(f)["abi"]

class LockContract:
    def __init__(self, address, abi, web3, signer):
        self.address = address
        self.abi = abi
        self.web3 = web3
        self.signer = signer
        self.contract = web3.eth.contract(address=address, abi=abi)

    def withdraw(self):
        tx = self.contract.functions.withdraw().build_transaction({
            "from": self.signer,
            "nonce": self.web3.eth.get_transaction_count(self.signer),
            "gas": 200000,
            "gasPrice": self.web3.to_wei("20", "gwei"),
        })
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key=os.getenv("PRIVATE_KEY"))
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print("Sent withdraw transaction:", tx_hash.hex())
        return tx_hash

lock = LockContract(LOCK_ADDRESS, LOCK_ABI, web3, eth_client.signer)