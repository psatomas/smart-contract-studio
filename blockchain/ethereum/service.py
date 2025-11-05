from ethereum.contracts import get_unlock_time, withdraw

@app.get("/contract/unlock-time")
def read_unlock_time():
    return {"unlock_time": get_unlock_time()}

@app.post("/contract/withdraw")
def call_withdraw():
    receipt = withdraw()
    return {"tx_hash": receipt.transactionHash.hex()}