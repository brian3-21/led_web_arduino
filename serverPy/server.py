import asyncio
import websockets
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)


PORT = 8765

# Función para escribir y leer datos desde el Arduino
def sendArduino(x):
    arduino.write(bytes(x, 'utf-8'))  # Enviar datos al Arduino
    time.sleep(0.05)  # Esperar un breve periodo de tiempo

def sendData(data):
    if data == "P":
        print("Se ha prendido")
        sendArduino(data)
    elif data == "N":
        print("Se ha apagado")
        sendArduino(data)

    return data


class WebSocketServer:
    def __init__(self):
        self.data = None # Inicializa el atributo de instancia para el estado del LED

    async def hello(self, websocket):
        try:
            
            recived = await websocket.recv()
            print(f"<<< {recived}")
            self.data = sendData(recived)
            await websocket.send(self.data)
            print(f"<<< El mensaje enviado es: {self.data}")
        except websockets.exceptions.ConnectionClosed as errorCC:
            print("Se ha desconectado alguien")



    async def main(self):
        async with websockets.serve(self.hello, "localhost", PORT):
            await asyncio.Future() # run forever
    
    

if __name__ == "__main__":
    server = WebSocketServer()
    print("Corriendo servidor en el puerto: " + str(PORT))
    asyncio.run(server.main())

