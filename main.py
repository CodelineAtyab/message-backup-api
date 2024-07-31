import uuid
import socket
import traceback

import uvicorn

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator


NODE_ID = str(uuid.uuid4())

try:
    NODE_ID = socket.gethostname()
except Exception:
    print("Unable to get hostname")
    print(traceback.format_exc())

app = FastAPI()

# Instrument the FastAPI app
Instrumentator().instrument(app).expose(app)

@app.get('/')
def status():
    return {"node_id": NODE_ID}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
