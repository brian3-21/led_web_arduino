// Función para enviar comandos al servidor
function enviarComando(comando) {
    const socket = new WebSocket('ws://localhost:8765'); // Cambia la URL según tu servidor

    // Escucha los eventos del socket
    socket.addEventListener('open', (event) => {
        console.log('Conexión establecida con el servidor');
        socket.send(comando); // Envía el comando al servidor
    });

    socket.addEventListener('message', (event) => {
        console.log('Respuesta del servidor:', event.data);
        // Aquí puedes manejar la respuesta del servidor si es necesario
    });

    socket.addEventListener('close', (event) => {
        console.log('Conexión cerrada con el servidor');
    });
}