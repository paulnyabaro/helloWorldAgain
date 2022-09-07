import requests, bs4, webbrowser

search_term = input('Enter the search term you want: ')
print('Searching...')

res = requests.get(f'https://google.com/search?q={search_term}')
webbrowser.open(f'https://google.com/search?q={search_term}')
res.raise_for_status()
print(res)

search_result = bs4.BeautifulSoup(res.text)
link_elements = search_result.select('.g')
print(link_elements)