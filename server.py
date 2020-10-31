import asyncio
import serial
import keyboard
import sys
import time
import websockets
async def echo(websocket, path):
    async for message in websocket:
        message = str(message)
        print(message)
        await websocket.send(message)
        if message:
            serArd.write((message).encode())
            myData = serArd.readline().decode()
            print(myData)
        else:
            serArd.write(('0').encode())
            myData = serArd.readline().decode()
            print(myData)
        time.sleep(0.05)
start_server = websockets.serve(echo, "192.168.0.100", 8765)
with serial.Serial("COM3",9600) as serArd:
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
