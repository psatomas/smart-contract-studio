from .client import EthereumClient

eth_client = EthereumClient()

def deploy_dummy_contract():
    if not eth_client.is_connected():
        raise ConnectionError("Ethereum client not connected")
    return "0xDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEF"

def get_contract_balance(address: str):
    if not eth_client.is_connected():
        raise ConnectionError("Ethereum client not connected")
    return 1234567890