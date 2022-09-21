import pyautogui, time, webbrowser

webbrowser.open('https://kleki.com/')

time.sleep(5)
# click to put drawing program in focus



def draw_triangle():
    distance = 300
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=1)
        # move right
        distance = distance - 10
        pyautogui.dragRel(0, distance, duration=1)
        # move down
        pyautogui.dragRel(-distance, 0, duration=1)  # move left
        distance = distance - 10
        pyautogui.dragRel(0, -distance, duration=1)  # move up


pyautogui.click(300, 450, duration=0.25)
draw_triangle()
# time.sleep(5)
pyautogui.click(600, 450, duration=0.25)
draw_triangle()
# time.sleep(5)
pyautogui.click(300, 150, duration=0.25)
draw_triangle()
# time.sleep(5)
pyautogui.click(600, 150, duration=0.25)
draw_triangle()

# Scrolling up and down
# pyautogui.scroll(200) # for up use -200

