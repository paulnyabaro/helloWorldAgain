import pyautogui

img = pyautogui.screenshot()
print(img)
print(img.getpixel((50, 200)))

# Seeing if the area matches the pixels
print(pyautogui.pixelMatchesColor(50, 200, (60, 63, 65)))
print(pyautogui.pixelMatchesColor(50, 200, (130, 135, 144)))

# Clicking a specific position from a taken screenshot
print(pyautogui.locateOnScreen('example-image.jpg'))
# if image is a even a pixel off, None will be returned
