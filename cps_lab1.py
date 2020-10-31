import serial
import keyboard
import sys
import time

LED_flag = False
with serial.Serial("COM3",9600) as serArd:
    print(f"The Arduino board is connect through {serArd.port}")
    while True:
        # try:
            # con_val = input(f"Enter 1 for turn on LED and 0 for turn off LED : ")
            # while not con_val in ['a','s','d','w','q','0']:
            #     print(f"Please enter 1 or 0 !")
            #     con_val = input(f"Enter 1 for turn on LED and 0 for turn off LED : ")
            # print(f"You entered {con_val}")
            if keyboard.is_pressed('a'):
                serArd.write(('a').encode())
                myData = serArd.readline().decode()
                print(myData)
            # serArd.write(('0').encode())
            # myData = serArd.readline().decode()
            # print(myData)
            if keyboard.is_pressed('s'):
                serArd.write(('s').encode())
                myData = serArd.readline().decode()
                print(myData)
            # if keyboard.is_pressed('s') and keyboard.is_pressed('d'):
            #     serArd.write(('y').encode())
            #     myData = serArd.readline().decode()
            #     print(myData)
            # if keyboard.is_pressed('s') and keyboard.is_pressed('a'):
            #     serArd.write(('t').encode())
            #     myData = serArd.readline().decode()
            #     print(myData)
            if keyboard.is_pressed('d'):
                serArd.write(('d').encode())
                myData = serArd.readline().decode()
                print(myData)
            if keyboard.is_pressed('w'):
                serArd.write(('w').encode())
                myData = serArd.readline().decode()
                print(myData)
            # if keyboard.is_pressed('w') and keyboard.is_pressed('a'):
            #     serArd.write(('e').encode())
            #     myData = serArd.readline().decode()
            #     print(myData)
            # if keyboard.is_pressed('w') and keyboard.is_pressed('d'):
            #     serArd.write(('r').encode())
            #     myData = serArd.readline().decode()
            #     print(myData)
            
            if keyboard.is_pressed('esc'):
                serArd.write(('0').encode())
                myData = serArd.readline().decode()
                print(myData)
                serArd.close()
                break
            time.sleep(0.05)
            # if(serArd.writable() and con_val != 'q'):
            #     serArd.write(con_val.encode())
            #     myData = serArd.readline().decode()
            #     print(myData)
            # if con_val == 'q':
            #     print("Program is stopped!")
            #     serArd.close()
            #     break
        # except serial.SerialException as er:
        #     print(er)
        # except KeyboardInterrupt:
        #     serArd.close()
        #     sys.exit(0)