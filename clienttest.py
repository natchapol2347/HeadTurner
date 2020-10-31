import asyncio
import websockets
import keyboard
import msvcrt
import time

async def send(key):
    uri = "ws://192.168.0.100:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(key)
        print(await websocket.recv())




while True:
    key=msvcrt.getch()
    key = str(key)[-2]
    print(key)
    asyncio.get_event_loop().run_until_complete(send(key))
    time.sleep(0.1)
    
        