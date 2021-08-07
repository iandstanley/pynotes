import unittest
import os
import gnupg
from dotenv import load_dotenv
load_dotenv(override=True)
from pynoteslib import *
#import pynoteslib
#import pudb; pu.db

TESTKEY = 'E4D4E23B3AC48FFA15C1949216427604C30E9831'
FAKEKEY = 'Not Really a GPG key'

class TestNoteEncryptAndDecrypt(unittest.TestCase):
    def test_encrypt_and_decrypt(self):
        message = "This is some text"
        n = Notes(title='testing encrypt')
        n.set_plaintext(message)
        ct = n.encrypt()
        n.save_ciphertext()
        self.assertTrue( os.path.exists(get_note_fullpath(n.filename)))
        pt = n.decrypt()
        self.assertEqual(message, pt)

class TestValidateKey(unittest.TestCase):
    def test_validate_gpg_key(self):
        self.assertTrue(validate_gpg_key(TESTKEY))
        self.assertFalse(validate_gpg_key(FAKEKEY))
