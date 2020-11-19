import asyncio
import serial
import keyboard
import sys
import time
import websockets
# analog=[]
# rotation=[]
# buttons=[]
async def echo(websocket, path):
    global go_x,go_y,turn_x,turn_y,square,x,o,triangle
    go_x=0
    go_y=0
    turn_x=0
    turn_y=0
    square=False
    x=False
    o=False
    triangle=False
    async for message in websocket:
        message = str(message)
        print(message)
        if(message[0] == 'A'):
            analog=message.split()
            go_x = analog[1]
            go_y = analog[2]
            turn_x = analog[3]
        if(message[0] == 'R'):
            rotation=message.split()
            turn_y = rotation[1]
        if(message[0] == 'B'):
            button=message.split()
            square = button[1]
            x = button[2]
            o = button[3]
            triangle = button[4]

        asyncio.get_event_loop().create_task(arduino(websocket, path))
        # serArd.write((go_y).encode())
        
        # if message:
        #     serArd.write((message).encode())
        #     myData = serArd.readline().decode()
        #     print(myData)
        # else:
        #     serArd.write(('0').encode())
        #     myData = serArd.readline().decode()
        #     print(myData)
        # await asyncio.sleep(0.05)
async def arduino(websocket, path):
    
    serArd.write((go_x).encode())
    await websocket.send(serArd.readline().decode())
    
    # await asyncio.sleep(1)
    # print("Hey babe")


global serArd
serArd=serial.Serial()
serArd.baudrate=9600
serArd.port='COM5'
serArd.open()
start_server = websockets.serve(echo, "10.100.11.75", 8765)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
