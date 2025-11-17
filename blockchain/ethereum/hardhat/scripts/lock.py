from web3 import Web3
import json
import os

# ---------------------------
# Web3 Connection
# ---------------------------
RPC_URL = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.is_connected():
    raise ConnectionError(f"Cannot connect to Ethereum node at {RPC_URL}")

# Use first account from Hardhat node
signer = web3.eth.accounts[0]

# ---------------------------
# Load Contract ABI
# ---------------------------
ABI_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "hardhat",
    "artifacts",
    "contracts",
    "Lock.sol",
    "Lock.json"
)

with open(ABI_PATH, "r") as f:
    data = json.load(f)
    abi = data["abi"]

# Contract deployed address
CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)


# ---------------------------
# Withdraw Function
# ---------------------------
def withdraw():
    tx = contract.functions.withdraw().build_transaction({
        "from": signer,
        "nonce": web3.eth.get_transaction_count(signer),
        "gas": 200000,
        "gasPrice": web3.eth.gas_price
    })

    signed = web3.eth.account.sign_transaction(tx, private_key=None)  # Hardhat auto-sign
    # If using Hardhat, sending *unsigned* tx works because node auto-signs local calls:
    tx_hash = web3.eth.send_transaction(tx)

    return tx_hash