import pyautogui

img = pyautogui.screenshot()
print(img)
print(img.getpixel((50, 200)))

# Seeing if the area matches the pixels
print(pyautogui.pixelMatchesColor(50, 200, (60, 63, 65)))
print(pyautogui.pixelMatchesColor(50, 200, (130, 135, 144)))

# Clicking a specific position from a taken screenshot
print(pyautogui.locateOnScreen('example-image.jpg'))
# if the image is even a pixel off, None will be returned otherwise it will return a Generator object
# [(643, 745, 70, 29), (1007, 801, 70, 29)] returned if found on several places
# then pyautogui.center((643, 745, 70, 29)) and  pyautogui.click((678, 759))
