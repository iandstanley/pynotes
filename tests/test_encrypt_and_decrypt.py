import unittest
import os
from dotenv import load_dotenv
load_dotenv(override=True)
from pynoteslib import *
#import pynoteslib
#import pudb; pu.db


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