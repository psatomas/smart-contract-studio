from web3 import Web3

class EthereumClient:
    def __init__(self, rpc_url="http://127.0.0.1:8545"):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.connected = self.web3.is_connected()
        if not self.connected:
            raise ConnectionError(f"Cannot connect to Ethereum node at {rpc_url}")
        # Use the first account as default signer
        self.signer = self.web3.eth.accounts[0]

    def is_connected(self):
        return self.connected

    def get_signer(self):
        return self.signer

    def get_balance(self, address=None):
        if address is None:
            address = self.signer
        return self.web3.eth.get_balance(address)