import pyautogui, time
time.sleep(2)
# click to put drawing program in focus



def draw_triangle():
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.9)
        # move right
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.9)
        # move down
        pyautogui.dragRel(-distance, 0, duration=0.9)  # move left
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=0.9)  # move up


pyautogui.click(300, 400, duration=0.25)
draw_triangle()
time.sleep(10)
pyautogui.click(500, 400, duration=0.25)
draw_triangle()
time.sleep(10)
pyautogui.click(300, 200, duration=0.25)
draw_triangle()
time.sleep(10)
pyautogui.click(500, 200, duration=0.25)
draw_triangle()

# Scrolling up and down
pyautogui.scroll(200) # for up use -200