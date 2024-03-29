import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status() # Always use this to make sure it downloads before you continue
print(res)
print(len(res.text))
print(res.text[:250])

# using the try and except to handle errors
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

# Writing to a file
# the b in wb stands for binary
# data instead of text data in order to maintain the Unicode encoding of the text
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
    # The iter_content() method returns “chunks” of the content on each iteration through the loop

playFile.close()