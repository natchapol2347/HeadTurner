import RPi.GPIO as GPIO
import time
import keyboard
used_pin = (8, 10, 12,16)
used_pin_2 = (2, 3, 4, 17)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(used_pin, GPIO.OUT)
GPIO.setup(used_pin, GPIO.OUT)

step = [[1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1]
       ]
while True:
    for i in step:
        for j in range(4):
            #GPIO.output(used_pin[j], i[j])
            print(used_pin[j], i[j])

