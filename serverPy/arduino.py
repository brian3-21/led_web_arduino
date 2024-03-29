import asyncio
import websockets

url = "ws://localhost:8765"

async def resp():
    while True:
            ws = websockets.connect(url)
            websocket.send("Hello world!")
            message = ws.recv()
            await print(f"Received: {message}")

asyncio.run(resp())