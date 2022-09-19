import smtplib
# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print(type(smtpObj))
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('cit2270312015@mmu.ac.ke', 'Pass1234')
smtpObj.sendmail('cit2270312015@mmu.ac.ke', 'barrowspace@gmail.com', 'Subject: Testing smtplib module.\n'
                    'Hey there, am tryinto see if this is working')