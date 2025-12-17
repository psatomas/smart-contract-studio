import requests
from django.conf import settings

BLOCKCHAIN_URL = getattr(settings, "BLOCKCHAIN_URL", "http://blockchain:9000")

def blockchain_health():
    try:
        return requests.get(f"{BLOCKCHAIN_URL}/health/blockchain", timeout=5).json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_unlock_time():
    try:
        return requests.get(f"{BLOCKCHAIN_URL}/contract/unlock-time", timeout=5).json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

def withdraw_lock():
    try:
        return requests.post(f"{BLOCKCHAIN_URL}/contracts/lock/withdraw", timeout=10).json()
    except Exception as e:
        return {"status": "error", "message": str(e)}
