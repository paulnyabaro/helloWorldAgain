import requests, bs4

res = requests.get('https://kipkatam.com')
# res = requests.get('http://nostarch.com')
print(res.raise_for_status())
print(res)

webContent = bs4.BeautifulSoup(res.text)
print(type(webContent))

#Passing an html page locally
# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile)
# type(exampleSoup)

# Soup select
# soup.select('div')

links = webContent.select('a')
print(links)