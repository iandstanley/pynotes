import gnupg

gpg = gnupg.GPG(gnupghome='/home/ian/.gnupg')

print(gpg)

message = """
Copyright (c) 2021, Ian Stanley
All rights reserved.
This is a demo message
"""

recipients = 'test@noteslib'
#recipients = 'E4D4E23B3AC48FFA15C1949216427604C30E9831'

data = gpg.encrypt(message, recipients)

print (data.ok)
print (data.status)
print (f"data = \n {str(data)}")

checkmsg = gpg.decrypt(str(data))

print (checkmsg)




