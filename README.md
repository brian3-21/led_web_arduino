# led_web_arduino

This project consists of a web client with HTML and JavaScript that connects to a socket server built in Python. The server receives the signal from the web page and sends it to an Arduino board.

## Features

- Web client with HTML and JavaScript that allows controlling an LED.
- Socket server in Python that receives the signals from the web client and sends them to the Arduino board.
- Integration with an Arduino board to control a physical LED.

## Requirements

- Python 3.x
- Python socket library (included in the standard library)
- Python WebSockets library (e.g., `websocket-client`)
- Arduino IDE
- Arduino-compatible board
