import joystickapi
import msvcrt
import time
import asyncio
import websockets

print("start")

num = joystickapi.joyGetNumDevs()
ret, caps, startinfo =False, None, None
for id in range(num):
    ret, caps = joystickapi.joyGetDevCaps(id)
    if ret:
        print("gamepad detected: " + caps.szPname)
        ret, startinfo = joystickapi.joyGetPosEx(id)
        break
else:
    print("no gamepad detected")

# Python program to convert a list to string 
	
def listToString(s):
    str1=''
    for ele in s:
        ele = str(ele)
        str1+=" "+ele
    return str1
    

		
		
async def sendEvent():
    uri= "ws://localhost:8765"
    async with websockets.connect(uri, ping_interval=None) as websocket:
        while True:
            await asyncio.sleep(0.1)
            # if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode(): # detect ESC         
            ret, info = joystickapi.joyGetPosEx(id)
            if ret:
                btns = [(1 << i) & info.dwButtons != 0 for i in range(caps.wNumButtons)]
                axisXYZ = [info.dwXpos-startinfo.dwXpos, info.dwYpos-startinfo.dwYpos, info.dwZpos-startinfo.dwZpos]
                axisRUV = [info.dwRpos-startinfo.dwRpos, info.dwUpos-startinfo.dwUpos, info.dwVpos-startinfo.dwVpos]
                if info.dwButtons:
                    # print("buttons: ", btns)
                    print("buttons: ", listToString(btns))

                    await websocket.send('B'+listToString(btns))
                    await websocket.recv()

                if any([abs(v) > 10 for v in axisXYZ]):
                    # print("axis:", axisXYZ)
                    print("axis:", listToString(axisXYZ))
                    await websocket.send('A'+listToString(axisXYZ))
                    await websocket.recv()

                if any([abs(v) > 10 for v in axisRUV]):
                    # print("rotation axis:", axisRUV)
                    print("roation axis:", listToString(axisRUV))
                    await websocket.send('R'+listToString(axisRUV))
                    await websocket.recv()
            

asyncio.run(sendEvent())
        

