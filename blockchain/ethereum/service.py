from fastapi import APIRouter
from blockchain.ethereum.contracts import get_lock_contract

router = APIRouter(prefix="/contract", tags=["contract"])

@router.get("/unlock-time")
def read_unlock_time():
    lock = get_lock_contract()
    return {"unlock_time": lock.unlock_time()}

@router.post("/withdraw")
def withdraw():
    lock = get_lock_contract()
    receipt = lock.withdraw()
    return {"tx_hash": receipt.transactionHash.hex()}