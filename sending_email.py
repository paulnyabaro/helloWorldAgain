import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# Optional if SMTP is not working
# smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# Determining type
print(type(smtpObj))

# Greetings to the server
print(smtpObj.ehlo())

# Enabling encryption if using port 587 but if 465, encryption already established
print(smtpObj.starttls())

# This is a more secure method than storing them on the code
# or what if I use a hashed format
email_address = input('Enter your email address ')
email_password = input('Enter password ')
print(smtpObj.login(f'{email_address}', f'{email_password}'))

# Multiple recipient emails can be added
print(smtpObj.sendmail('example@mail.com', 'exampletwo@mail.com', 'Subject: Testing smtplib module.\n'
                    'Hey there, am tryinto see if this is working'))

# The result will be a dictionary of the delivery statuses to the recipient address(es)
# '\n' separates the subject from the body
