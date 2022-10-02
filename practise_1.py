import requests, webbrowser, pyautogui, time

url = 'https://b-ok.africa/'
open_google = requests.get(url)
print(open_google)
webbrowser.open(url)

time.sleep(5)
pyautogui.typewrite('Things fall apart', 0.2)
pyautogui.press('enter')