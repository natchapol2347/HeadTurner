import RPi.GPIO as GPIO
import time
from pynput import keyboard
used_pin = (8, 10, 12,16)
used_pin_2 = (3, 5, 7, 11)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(used_pin, GPIO.OUT)
GPIO.setup(used_pin_2, GPIO.OUT)

step = [[1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1]
       ]
used_pin = (8, 10, 12,16)
used_pin_2 = (3, 5, 7,11)
h_step = 0
v_step = 0
left = False
right = False
def on_press(key):
    try:
        global h_step
        global v_step
        if keyboard.Key.left == key:
            for i in range(4):
                print(used_pin[i], step[h_step][i])
            h_step -= 1
        elif keyboard.Key.right == key:
            for i in range(4):
                print(used_pin[i], step[h_step][i])
        if keyboard.Key.up == key:
            for i in range(4):
                print(used_pin_2[i], step[v_step][i])
            v_step -= 1
        elif keyboard.Key.down == key:
            for i in range(4):
                print(used_pin_2[i], step[v_step][i])
            v_step += 1
        if h_step < 0:
            h_step = 7
        if h_step > 7:
            h_step = 0
        if v_step < 0:
            v_step = 7
        if v_step > 7:
            v_step = 0
                
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press,
                       on_release=on_release) as listener:
    listener.join()


