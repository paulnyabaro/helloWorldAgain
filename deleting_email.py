import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')
imapObj.select_folder('INBOX', readonly=True) UIDs = imapObj.search(['SINCE 05-Jul-2014'])
rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
# import pyzmail
# message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
# message.get_subject()
#  pyzmail has issue installing

# 'ALL'Returns all messages in the folder. You may run in to imaplib
# size limits if you request all the messages in a large folder. See
# “Size Limits” on page 371.
# 'BEFORE date',
# 'ON date',
# 'SINCE date'These three search keys return, respectively, messages that
# were received by the IMAP server before, on, or after the
# given date. The date must be formatted like 05-Jul-2015.
# Also, while 'SINCE 05-Jul-2015' will match messages on
# and after July 5, 'BEFORE 05-Jul-2015' will match only mes-
# sages before July 5 but not on July 5 itself.
# 'SUBJECT string',
# 'BODY string',
# 'TEXT string'Returns messages where string is found in the subject, body,
# or either, respectively. If string has spaces in it, then enclose
# it with double quotes: 'TEXT "search with spaces"'.
# (continued)
# Sending Email and Text Messages    369Table 16-3 (continued)
# Search keyMeaning
# 'FROM string',
# 'TO string',
# 'CC string',
# 'BCC string'Returns all messages where string is found in the “from”
# emailaddress, “to” addresses, “cc” (carbon copy) addresses,
# or “bcc” (blind carbon copy) addresses, respectively. If there
# are multiple email addresses in string, then separate them
# with spaces and enclose them all with double quotes:
# 'CC "firstcc@example.com secondcc@example.com"'.
# 'SEEN',
# 'UNSEEN'Returns all messages with and without the \Seen flag, respec-
# tively. An email obtains the \Seen flag if it has been accessed
# with a fetch() method call (described later) or if it is clicked
# when you’re checking your email in an email program or web
# browser. It’s more common to say the email has been “read”
# rather than “seen,” but they mean the same thing.
# 'ANSWERED',
# 'UNANSWERED'Returns all messages with and without the \Answered flag,
# respectively. A message obtains the \Answered flag when it
# is replied to.
# 'DELETED',
# 'UNDELETED'Returns all messages with and without the \Deleted flag, respec-
# tively. Email messages deleted with the delete_messages()
# method are given the \Deleted flag but are not permanently
# deleted until the expunge() method is called (see “Deleting
# Emails” on page 375). Note that some email providers, such
# as Gmail, automatically expunge emails.
# 'DRAFT',
# 'UNDRAFT'Returns all messages with and without the \Draft flag, respec-
# tively. Draft messages are usually kept in a separate Drafts
# folder rather than in the INBOX folder.
# 'FLAGGED',
# 'UNFLAGGED'Returns all messages with and without the \Flagged flag,
# respectively. This flag is usually used to mark email mes-
# sages as “Important” or “Urgent.”
# 'LARGER N',
# 'SMALLER N'Returns all messages larger or smaller than N bytes,
# respectively.
# 'NOT search-key'Returns the messages that search-key would not have returned.
# 'OR search-key1
# search-key2'Returns the messages that match either the first or second
# search-key.


# imapObj.search(['ALL'])
# Returns every message in the currently
# selected folder.
# imapObj.search