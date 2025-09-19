class EthereumClient:
    def __init__(self):
        self.connected = True

    def is_connected(self):
        return self.connected