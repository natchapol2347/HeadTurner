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
            square = button[1] 
            x = button[2] 
            o = button[3] 
            triangle = button[4]
        else:
            square = 'False'
            x = 'False'
            o = 'False'
            triangle = 'False'

        await asyncio.get_running_loop().run_in_executor(None, arduino)
      


def arduino():
    ser = serial.Serial('COM8', 9600, timeout=1)
    # values=bytearray([mapping(go_x),mapping(go_y),mapping(turn_x),mapping(turn_y),bool_convert(square),bool_convert(x),bool_convert(o),bool_convert(triangle)])
    values=mapping(go_x)
    ser.write(values.encode())
    # print(ser.read().decode)
    
def mapping(value, in_min=-32767, in_max=32767, out_min=0, out_max=255):
    if(value<=32767 and value>=-32767):
        return (value-in_min)*(out_max-out_min)//(in_max-in_min)+out_min
    else:
        return 127
def bool_convert(value):
    if value=='True':
        # print("yay")
        return 1
    else:
        # print('yay)')
        return 0
    
    
    
    
    
    
    
    



start_server = websockets.serve(echo, "10.100.11.75", 8765)

 
asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()