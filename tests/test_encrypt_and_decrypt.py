import unittest
import os
from dotenv import load_dotenv
load_dotenv(override=True)
from pynoteslib import *
#import pynoteslib
#import pudb; pu.db


class TestNoteEncryptAndDecrypt(unittest.TestCase):
    def test_encrypt(self):
        n = Notes(title='testing encrypt')
        n.set_plaintext("This is some text")
        n.encrypt()
        n.save_ciphertext()
        self.assertTrue( os.path.exists(get_note_fullpath(n.filename)))

    def test_decrypt(self):
        n = Notes(title="testing decrypt")
        n.set_ciphertext("%% This is some text")
        n.decrypt()
        n.save_plaintext()
        self.assertTrue(os.path.exists(get_note_fullpath("testing_decrypt")))
