const WebSocket = require("ws");

const wss = new WebSocket.Server({ port: 8080 });

console.log("WebSocket Server Running on ws://localhost:8080");

wss.on("connection", (ws) => {
    console.log("Client connected");

    setInterval(() => {
        const sensorData = {
            temperature: (Math.random() * 30 + 10).toFixed(2),
            humidity: (Math.random() * 50 + 20).toFixed(2),
        };
        ws.send(JSON.stringify(sensorData));
    }, 2000);

    ws.on("close", () => console.log("Client disconnected"));
});
