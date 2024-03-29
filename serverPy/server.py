import asyncio
import websockets

class WebSocketServer:
    def __init__(self):
        self.data = None # Inicializa el atributo de instancia para el estado del LED

    async def hello(self, websocket):
        recived = await websocket.recv()
        print(f"<<< {recived}")

        if recived == 'P':
            print("Has encendido el LED")
            self.data = 'P'
        elif recived == 'N':
            print("Has apagado el led")
            self.data = 'N'

        await websocket.send(self.data)
        print(f"<<< El mensaje enviado es: {self.data}")
        
    async def main(self):
        async with websockets.serve(self.hello, "localhost", 8765):
            await asyncio.Future() # run forever

if __name__ == "__main__":
    server = WebSocketServer()
    asyncio.run(server.main())
