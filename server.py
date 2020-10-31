import asyncio
import logging
import websockets
from websockets import WebSocketServerProtocol

logging.basicConfig(level=logging.INFO)


async def produce(message:str, hostname: str, port: int) -> None:
    websocket_resource_url= f"ws://{hostname}:{port}"
    async with websockets.connect(websocket_resource_url) as ws:
        await ws.send(message)
        await ws.rcv()


class Server:
    clients = set()
    
    async def register(self,ws:WebSocketServerProtocol) -> None:
        self.clients.add(ws)
        logging.info(f"{ws.remote_address} disconnects.")

    async def unregister(self,ws:WebSocketServerProtocol) -> None:
        self.clients.remove(ws)
        logging.info(f"{ws.remote_address} disconnects.")
    async def send_to_clients(self, message:str) -> None:
        if self.clients:
            await asyncio.wait([client.send(message) for client in self.clients])
    async def ws_handler(self, ws: WebSocketServerProtocol, uri:str) -> None:
        await self.register(ws)
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)
    async def distribute(self, ws:WebSocketServerProtocol)-> None:
        async for message in ws:
            await self.send_to_clients(message)




asyncio.run(produce(message='hi', hostname='localhost', port=4000))
start = Server()
start_server = websockets.serve(server.ws_handler,"localhost",port=4000)
loop.run_until_complete(start_server)
loop.run_forever()