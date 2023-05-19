import logging
import asyncio
from fastapi import FastAPI, WebSocket
import random
from random import seed

seed(1)

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(3.5)
        
        #puntos de interes de limache
        latitud = round(random.uniform(-33.032, -32.98), 6)
        longitud = round(random.uniform(-71.27, -71.22), 6)
        lat_lon_string = { 'latitud':"{:.6f}".format(latitud), 'longitud':"{:.6f}".format(longitud)}
        await websocket.send_json(lat_lon_string)