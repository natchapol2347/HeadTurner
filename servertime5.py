import asyncio
import serial
import keyboard
import sys
import time
import websockets
import struct
import threading
from pySerialTransfer import pySerialTransfer as txfer

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
        await asyncio.sleep(0.1)
        arduino()

      



def arduino():
    # values=struct.pack('>BBBBBBBB',mapping(go_x),mapping(go_y),mapping(turn_x),mapping(turn_y),bool_convert(square),bool_convert(x),bool_convert(o),bool_convert(triangle))
    # print(struct.unpack('>BBBBBBBB',values))
    # values=f"{mapping(go_x)},{mapping(go_y)},{mapping(turn_x)},{mapping(turn_y)},{bool_convert(square)},{bool_convert(x)},{bool_convert(o)},{bool_convert(triangle)},"
    values=[mapping(go_x),mapping(go_y),mapping(turn_x),mapping(turn_y),bool_convert(square),bool_convert(x),bool_convert(o),bool_convert(triangle)]

    print(values)
    list_=link.tx_obj(values)
    link.send(list_)
    
    
def mapping(value, in_min=-32767, in_max=32767, out_min=0, out_max=255):
    if(value<=32767 and value>=-32767):
        new_value=(value-in_min)*(out_max-out_min)//(in_max-in_min)+out_min
        return new_value
    elif(value>32767):
        return 255
    elif(value<-32767):
        return 0
def bool_convert(value):
    if value=='True':
        # print("yay")
        return True
    else:
        # print('yay)')
        return False
        
    
    
    
    
    
    
    
    

try:
    
    start_server = websockets.serve(echo, "10.100.4.128", 8765)

    link=txfer.SerialTransfer('COM7',9600)
    link.open()
    time.sleep(2) # allow some time for the Arduino to completely reset

    asyncio.get_event_loop().run_until_complete(start_server)
    

    asyncio.get_event_loop().run_forever()
except ConnectionError:
    print("Disconnected")
except KeyboardInterrupt:
    try:
        link.close()
    except:
        pass

except:
    import traceback
    traceback.print_exc()
    
    try:
        link.close()
    except:
        pass

finally:
    link.close()
    print("Unpaired")