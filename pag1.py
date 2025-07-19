import os
import time
import pyautogui as p

os.system('cls') # Clears terminal on Windows

#If you move your mouse to the top-left corner of the screen (0, 0),
# the script immediately raises an exception and stops.
p.FAILSAFE = True

print("Current mouse position:")
print(p.position())  # Shows Point(x=?, y=?)

print("Screen size:")
print(p.size())  # Shows Size(width=?, height=?)

print("Is (1292, 148) on screen?")
print(p.onScreen(1292, 148))  # True or False

p.PAUSE = 2.5  # Pause after pyautogui actions (not print statements)

# If you want a pause BEFORE checking mouse position again
time.sleep(2.5)

print("Mouse position again after 2.5 seconds:")
print(p.position())
p.PAUSE = 2.5

p.moveTo(500, 500, duration=4) 
# move mouse to XY coordinates over num_second seconds

p.moveRel(200, 200, duration=2)
# # move mouse relative to its current position
# So if your mouse is at (100, 100) and you run moveRel(200, 200), it will go to:
# New position = (100+200, 100+200) = (300, 300)

p.dragTo(100, 322, duration=5)  # drag mouse to XY
# # means it will select area from where mouse is being dragged.
# Drag from current position to (600, 300) over 2 seconds
# p.dragTo(600, 300, duration=2, button='left')

p.dragRel(500, 100, duration=5, button='left')  # drag mouse relative to its current position


# p.click(x=200, y=500, clicks=2, interval=0.2, button='left')