import asyncio
import websockets

async def listen():
    url = "ws://localhost:8765"

    async with websockets.connect(url) as ws:
        while True:    
            await ws.send( "piri ")
            resp = await ws.recv()
            print(resp)
            print("reponse")

asyncio.run(listen())