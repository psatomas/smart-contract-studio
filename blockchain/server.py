from fastapi import FastAPI
from ethereum.contracts import contract  # <-- uses the shared DummyContract instance

app = FastAPI(
    title="Blockchain Service",
    version="0.1.0"
)


# -------------------------
# System / Health Check
# -------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}


# -------------------------
# Contract Info Endpoint
# -------------------------
@app.get("/contract/info")
def get_contract_info():
    """
    Returns metadata about the current blockchain contract.
    """
    return contract.get_contract_info()


# -------------------------
# Contract Trigger Endpoint
# -------------------------
@app.post("/contract/trigger")
def trigger_contract_call():
    """
    Executes a contract function (simulated for now).
    """
    return contract.trigger()