import RPi.GPIO as GPIO
import time
import keyboard
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
x_step = 0
while True:
    for j in range(4):
        #GPIO.output(used_pin[x_step], i[j])
        print(used_pin[j], step[x_step][j])
    x_step += 1
    if x_step == 8:
        x_step = 0

