from random import randint
final_number = ''
games_dictionary = {
    '1':'1',
    '2':'X',
    '3':'2' 
}
for i in range(10):
    random_key = str((randint(1,3)))
    final_number += games_dictionary[random_key]

print (final_number)