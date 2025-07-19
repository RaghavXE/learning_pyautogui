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

# p.PAUSE = 2.5  # Pause after pyautogui actions (not print statements)

# If you want a pause BEFORE checking mouse position again
# time.sleep(2.5)

# print("Mouse position again after 2.5 seconds:")
print(p.position())
# p.PAUSE = 2.5

# p.moveTo(500, 500, duration=2) 
# move mouse to XY coordinates over num_second seconds

# p.moveRel(200, 200, duration=2)
# # move mouse relative to its current position
# So if your mouse is at (100, 100) and you run moveRel(200, 200), it will go to:
# New position = (100+200, 100+200) = (300, 300)

# p.dragTo(100, 322, duration=5)  # drag mouse to XY
# # means it will select area from where mouse is being dragged.
# Drag from current position to (600, 300) over 2 seconds
# p.dragTo(600, 300, duration=2, button='left')

# p.dragRel(500, 100, duration=5, button='left')  # drag mouse relative to its current position


# p.click(x=200, y=500, clicks=2, interval=0.2, button='left')

# p.rightClick(x=40, y=500)
# p.PAUSE = 2
# p.middleClick(x=45, y=200)
# p.PAUSE = 2
# p.doubleClick(x=80, y=600)
# p.PAUSE = 2
# p.tripleClick(x=90, y=400)

# Scroll down
# p.scroll(-300)
# print("Scrolled down.")

# time.sleep(2)

# # Scroll up
# p.scroll(300)
# print("Scrolled up.")

# # Move to x=500, y=500 and then scroll down
# p.scroll(-500, x=500, y=500)

# print("Moved and scrolled.")


# Scroll down slowly and smoothly
# for i in range(20):        # Scroll 20 times
#     p.scroll(-5)           # Scroll down 5 units (small step)
#     time.sleep(0.0001)        # Pause to make scroll slow
    
    
    
  # Scroll down little faster and less smooth
# for i in range(20):        # Scroll 20 times
#     p.scroll(-50)           # Scroll down 5 units (small step)
      
      
      
p.mouseDown(x=128, y=146, button='left')  # Press down (start of click/drag)
p.mouseUp(x=800, y=600, button='left')    # Release (end of click/drag)
# The reason your code is not selecting text is because pyautogui.mouseDown() 
# and mouseUp() do not move the mouse between the two points — they just press
# and release at whatever position the cursor is currently at (unless you 
# explicitly move the mouse).



#To select:

# Move to start point
p.moveTo(128, 146)
p.mouseDown(button='left')  # Press and hold the mouse button

# Move to end point (this is what actually selects)
p.moveTo(800, 600, duration=0.5)

# Release the mouse button
p.mouseUp(button='left')


#  OR use p.moveTo and p.dragTo function.
import pyautogui as p

p.moveTo(148, 170)  # Go to start position
p.dragTo(500, 500, duration=1, button='left')  # Drag while holding left mouse button

