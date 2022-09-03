import zipfile, os

os.getcwd()
exampleZip = zipfile.ZipFile('examples.zip')
exampleZip.namelist()
spamInfo = exampleZip.getinfo('examples.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
.compress_size, 2)))
exampleZip.close()