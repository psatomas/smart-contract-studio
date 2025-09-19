import unittest
from blockchain.ethereum import contracts

class TestEthereumContracts(unittest.TestCase):
    
    def test_deploy_dummy_contract(self):
        address = contracts.deploy_dummy_contract()
        self.assertIsInstance(address, str)
        self.assertTrue(address.startswith("0x"))
        self.assertEqual(len(address), 42)  # 0x + 40 hex chars
    
    def test_get_contract_balance(self):
        address = contracts.deploy_dummy_contract()
        balance = contracts.get_contract_balance(address)
        self.assertIsInstance(balance, int)
        self.assertGreaterEqual(balance, 0)

if __name__ == "__main__":
    unittest.main()