import logging
import asyncio
from fastapi import FastAPI, WebSocket
from random import seed, randint

seed(1)

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(1.1)
        payload = randint(0, 10)
        await websocket.send_json(payload)