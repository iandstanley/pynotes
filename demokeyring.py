import gnupg

gpg = gnupg.GPG(gnupghome='/home/ian/.gnupg')

private_keys = gpg.list_keys(True)

print(f"type of private_keys = {type(private_keys)}")

firstkey = private_keys[0]

print(f"type of firstkey = {type(firstkey)}")

firstkeyid = private_keys[0]['keyid']

print(firstkeyid)

