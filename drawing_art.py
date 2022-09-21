import pyautogui, time
time.sleep(2)
pyautogui.click()
# click to put drawing program in focus
distance = 200
# pyautogui.click(300, 400, duration=0.25)
# pyautogui.click(510, 400, duration=0.25)
# pyautogui.click(300, 190, duration=0.25)
pyautogui.click(510, 190, duration=0.25)
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)
    # move down
    pyautogui.dragRel(-distance, 0, duration=0.2) # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2) # move up