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
        #print(message)
        await websocket.send(message)
        if(message[0] == 'A'):
            analog=message.split()
            go_x = int(analog[1])
            go_y = int(analog[2])
            turn_x = int(analog[3])
        if(message[0] == 'R'):
            rotation=message.split()
            turn_y = int(rotation[1])
        if(message[0] == 'B'):
            button=message.split()
            square = int(button[1])
            x = int(button[2])
            o = int(button[3])
            triangle = int(button[4])

        await asyncio.get_running_loop().run_in_executor(None, arduino)
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
def arduino():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    values=bytearray([go_x//128,go_y//128,turn_x//128,turn_y//128,square//128,x//128,o//128,triangle//128])
    print(values)
    

    
    
    
    
    
    



start_server = websockets.serve(echo, "10.100.14.101", 8765)

 
asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()