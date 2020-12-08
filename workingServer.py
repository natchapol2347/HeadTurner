import asyncio
import serial
import keyboard
import sys
import time
import websockets
import struct
import threading



async def start_server(websocket, path):
    global ser
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
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
        thread = threading.Thread(target=arduino)
        thread.start()
        await asyncio.sleep(0.1)
      



def arduino():
    values=struct.pack('>BBBBBBBB',mapping(go_x),mapping(go_y),mapping(turn_x),mapping(turn_y),bool_convert(square),bool_convert(x),bool_convert(o),bool_convert(triangle))
    # print(struct.unpack('>BBBBBBBB',values))
    # values=f"{mapping(go_x)},{mapping(go_y)},{mapping(turn_x)},{mapping(turn_y)},{bool_convert(square)},{bool_convert(x)},{bool_convert(o)},{bool_convert(triangle)},"
    # values = f"{go_x},{go_y},{turn_x},{turn_y},{square},{x},{o},{triangle},"
    ser.write(values)
    print(values)
    
    
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
        return 1
    else:
        # print('yay)')
        return 0
    
import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


#Display IP on LCD for Pi
# from RPLCD import CharLCD
# import fcntl

# lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

# def get_ip_address(ifname):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     return socket.inet_ntoa(fcntl.ioctl(
#         s.fileno(),
#         0x8915, 
#         struct.pack('256s', ifname[:15])
#     )[20:24])

# lcd.write_string("IP Address:") 

# lcd.cursor_pos = (1, 0)
# lcd.write_string(get_ip_address('wlan0') 
    
    
    
    
    
    

try:
    time.sleep(5)

    start_server = websockets.serve(start_server, get_ip(), 8765)

    
    asyncio.get_event_loop().run_until_complete(start_server)
    

    asyncio.get_event_loop().run_forever()
except ConnectionError:
    print("Disconnected")
finally:
    print("Unpaired")
