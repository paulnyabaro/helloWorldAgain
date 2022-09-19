import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')
imapObj.select_folder('INBOX', readonly=True) UIDs = imapObj.search(['SINCE 05-Jul-2014'])
rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
# import pyzmail
# message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
# message.get_subject()
#  pyzmail has issue installing