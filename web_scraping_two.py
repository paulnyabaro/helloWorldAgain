import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
    # Download the image.
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()


print('Done.')