with open('password.txt', 'r') as read_password:
    password = read_password.read()

user_password = input('Please enter you password to proceed ')
if user_password == password:
    print('Access granted')

elif user_password == '12345':
    print('This is what idiots use as password')

else:
    print('Access denied')
