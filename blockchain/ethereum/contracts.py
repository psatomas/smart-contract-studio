from abc import ABC, abstractmethod


class ContractInterface(ABC):
    @abstractmethod
    def get_contract_info(self):
        pass

    @abstractmethod
    def trigger(self):
        pass


class DummyContract(ContractInterface):
    def get_contract_info(self):
        return {
            "contract_name": "DummyContract",
            "address": "0x0000000000000000000000000000000000000000",
            "network": "localnet",
            "type": "dummy"
        }

    def trigger(self):
        return {
            "message": "Dummy contract trigger executed",
            "status": "success"
        }


contract = DummyContract()