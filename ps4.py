import keyboard 
import time
  
while True:  # making a loop
    if keyboard.is_pressed('a'):  # if key 'q' is pressed 
        print('Left')
    if keyboard.is_pressed('s'):  # if key 'q' is pressed 
        print('Back')
    if keyboard.is_pressed('d'):  # if key 'q' is pressed 
        print('Right')
    if keyboard.is_pressed('w'):  # if key 'q' is pressed 
        print('Forward')
    if keyboard.is_pressed('q'):
        break
    time.sleep(0.2)
