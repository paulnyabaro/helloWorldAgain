import requests, bs4

res = requests.get('https://www.jumia.co.ke/huawei-y5-lite-5.45-16gb-1gb-ram-3020-mah-single-sim-blue-72050054.html')
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

links = webContent.select('.-b.-ltr.-tal.-fs24')
print(links)