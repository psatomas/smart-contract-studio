from web3 import Web3
import os

class EthereumClient:
    def __init__(self):
        rpc_url = os.environ.get("ETH_RPC_URL", "http://localhost:8545")
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.account = self.web3.eth.accounts[0]  # first local Hardhat account

    def is_connected(self):
        return self.web3.is_connected()