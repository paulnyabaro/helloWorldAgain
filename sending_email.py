import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('bob@example.com', 'MY_SECRET_PASSWORD')
smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So long.\n'
                    'Dear Alice, so long and thanks for all the fish. Sincerely, Bob')