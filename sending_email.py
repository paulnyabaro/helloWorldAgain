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
print(smtpObj.login('example@mail.com', '12345678'))

smtpObj.sendmail('example@mail.com', 'exampletwo@mail.com', 'Subject: Testing smtplib module.\n'
                    'Hey there, am tryinto see if this is working')
