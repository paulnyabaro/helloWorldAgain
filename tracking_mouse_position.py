import pyautogui, random

# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr)
#         # print('\b' * len(positionStr), end='', flush=True)
#
# except KeyboardInterrupt:
#     print('\nDone')
#

# Clicking the mouse
# pyautogui.click(100, 150, button='right') # middle, left, secondary, primary
# Another option is pyautogui.mou![](transparentImage.png)seDown() and pyautogui.mouseUp()
# Others include
# pyautogui.doubleClick() , pyautogui.rightClick() and pyautogui.middleClick()

# Dragging the mouse
pyautogui.click(150,150, duration=0.25)
for i in range(100):
    pyautogui.dragTo(random.randint(150, 800), random.randint(150, 800), duration=0.25)
pyautogui.dragTo(150,150, duration=0.25)
# pyautogui.dragRel()