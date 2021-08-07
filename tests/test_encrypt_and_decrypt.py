import unittest
from pynoteslib import *
from dotenv import load_dotenv
load_dotenv(override=True)

#import pynoteslib
# import pudb; pu.db

TESTKEY1 = 'E4D4E23B3AC48FFA15C1949216427604C30E9831'
TESTKEY2 = '42456745CCBF000CA591E73CDBCC0C3D5CB54E7B'
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
        self.assertTrue(validate_gpg_key(TESTKEY1))
        self.assertTrue(validate_gpg_key(TESTKEY2))
        self.assertFalse(validate_gpg_key(FAKEKEY))

class TestNewKey(unittest.TestCase):
    def test_new_key(self):
        conf = get_config()
        # Create a note with TESTKEY1 (default in unittest)
        message = "This is some text to test new_key()"
        n = Notes(title='testing newkey')
        n.set_plaintext(message)
        ct = n.encrypt()
        n.save_ciphertext()
        self.assertTrue( os.path.exists(get_note_fullpath(n.filename)))
        # change all the notes to TESTKEY2
        success = new_key(TESTKEY2)
        self.assertTrue(success)
        note = Notes(filename='testing_newkey.asc')
        mess2 = n.decrypt()
        self.assertEqual(message, mess2)
        failure = new_key(FAKEKEY)
        self.assertFalse(failure)
