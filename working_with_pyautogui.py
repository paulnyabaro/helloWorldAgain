import pyautogui

# Handling errors
# us pyautogui.PAUSE = 1.5 to give you time to interrupt the process in case of an error
# PyAutoGUI also has a fail-safe feature. Moving the mouse cursor to the
# upper-left corner of the screen will cause PyAutoGUI to raise the pyautogui
# .FailSafeException exception --> disable this feature by pyautogui.FAILSAFE = False

print(pyautogui.size())

for i in range(5):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)