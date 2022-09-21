import pyautogui

# Handling errors
# us pyautogui.PAUSE = 1.5 to give you time to interrupt the process in case of an error
# PyAutoGUI also has a fail-safe feature. Moving the mouse cursor to the
# upper-left corner of the screen will cause PyAutoGUI to raise the pyautogui
# .FailSafeException exception --> disable this feature by pyautogui.FAILSAFE = False

print(pyautogui.size())
width, height = pyautogui.size()

for i in range(2):
    pyautogui.moveTo(1, 1, duration=0.25)
    pyautogui.moveTo(width - 1, 1, duration=0.25)
    pyautogui.moveTo(width - 1, height - 10, duration=0.25)
    pyautogui.moveTo(1, height -1, duration=0.25)

# Moving the mouse in relation to its current position
# pyautogui.moveRel(100, 0, duration=0.25)
for i in range(2):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)

# Getting the mouse position
print(pyautogui.position())