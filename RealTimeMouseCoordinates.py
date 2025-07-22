    
import pyautogui as p
import keyboard as k
import time

p.FAILSAFE = True
# i = 1

# while(i>0):
#     print(p.position())
#     p.PAUSE = 0.2



print("Tracking mouse... Press 'esc' to stop.")

while not k.is_pressed('esc'):
    print(p.position())
    time.sleep(0.2)


