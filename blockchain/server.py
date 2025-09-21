from fastapi import FastAPI
from ethereum import client, contracts   

app = FastAPI(title="Blockchain Service")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/contracts/dummy")
def get_dummy_contract():
    # Use your existing Ethereum client/contract code
    return {"address": contracts.deploy_dummy_contract()}