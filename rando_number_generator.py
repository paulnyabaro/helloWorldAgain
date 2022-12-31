from random import randint
final_number = ''
games_dictionary = {
    '1':'Y',
    '2':'N',
}
for i in range(13):
    random_key = str((randint(1,2)))
    final_number += games_dictionary[random_key]

print (final_number)
