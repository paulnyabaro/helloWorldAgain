import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
print(res)
print(len(res.text))
print(res.text[:250])