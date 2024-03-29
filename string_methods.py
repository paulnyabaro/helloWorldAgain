string_name = 'This is the name'
print(string_name.rjust(50, '*'))
print(string_name.ljust(50, '-'))
print(string_name.center(50, '+'))


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))