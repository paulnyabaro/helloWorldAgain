import pyautogui

img = pyautogui.screenshot()
print(img)
print(img.getpixel((50, 200)))

# Seeing if the area matches the pixels
print(pyautogui.pixelMatchesColor(50, 200, (60, 63, 65)))
print(pyautogui.pixelMatchesColor(50, 200, (130, 135, 144)))