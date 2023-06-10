from fastapi import WebSocket
from typing import Dict


class ConnectionManager:
    def __init__(self):
        #Keeps track of all the active connections
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, client_id: str, websocket: WebSocket):
        #Accepts a connection
        await websocket.accept()
        #Stores that websocket in dictionary for later use
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id):
        #we'll just remove the websocket from our dictionary
        del self.active_connections[client_id]

    async def send_personal_message(self, message: str, client_id: str):

        await self.active_connections[client_id].send_text(message)

    async def broadcast(self, message: str, client_to_exclude):
        #Broadcasting to everyone except the author.
        for client_id, connection in self.active_connections.items():
            if client_id == client_to_exclude:
                continue
            await connection.send_text(message)