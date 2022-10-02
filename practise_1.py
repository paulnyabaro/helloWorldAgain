import requests, webbrowser

url = 'https://google.com'
open_google = requests.get(url)
print(open_google)
webbrowser.open(url)