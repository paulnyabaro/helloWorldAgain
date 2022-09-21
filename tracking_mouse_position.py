import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
        # print(len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('Done')

