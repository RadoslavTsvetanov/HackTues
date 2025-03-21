import { WebSocket } from "ws";
import { context } from "../context";

const ws = new WebSocket("ws://localhost:8080");

ws.on("open", () => {
    console.log("Connected to WebSocket server");

    ws.on("message", (data: string) => {
        context
        console.log("Received:", data.toString());
    });

    // Send a notification after 2 seconds (to test thse "notify" functionality)
    setTimeout(() => {
        ws.send(JSON.stringify({
            type: "authenticate",
            payload: {
                member_id: "4e0973cf-8bcb-4fb5-bb16-4026b4ba852f",
                room_id: "feda0943-fde0-4020-b5d5-1cdc3a588340"
            }
        }));
    }, 2000);
    setInterval(() => {
        ws.send(JSON.stringify({
            type: "newData",
            payload: {
               member_id: "4e0973cf-8bcb-4fb5-bb16-4026b4ba852f",
            }
        }));
    }, 20000);
    
});

ws.on("close", () => console.log("Disconnected"));
