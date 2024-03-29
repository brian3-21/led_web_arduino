const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Manejo de conexiones WebSocket
io.on('connection', (socket) => {
    console.log('Cliente conectado');

    // Escucha los comandos enviados desde la página web
    socket.on('enviarComando', (comando) => {
        console.log('Comando recibido:', comando);
        // Aquí debes enviar el comando al Arduino a través del puerto serie
        // Puedes usar una biblioteca como 'serialport' para Node.js
    });
});

// Inicia el servidor en el puerto 3000 (puedes cambiarlo si lo deseas)
server.listen(3000, () => {
    console.log('Servidor escuchando en el puerto 3000');
});
