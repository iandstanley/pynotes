# TESTING NOTES

import unittest
import os
from pynoteslib import *
#import pynoteslib
#import pudb; pu.db

class TestNotesClassInitiators(unittest.TestCase):
    def test_nothing(self):
        pass

    def test_init(self):
        my = Notes()
        self.assertTrue(my.testinit)
        self.assertEqual(my.title, '')
        self.assertEqual(my.filename, '')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '')

    def test_init_with_title(self):
        my = Notes(title='this is my note title')
        self.assertEqual('this_is_my_note_title', my.title)
        self.assertEqual(my.filename, '')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '')

    def test_init_with_pt(self):
        my = Notes(title='my title', plaintext='Not so secret')
        self.assertEqual(my.title, 'my_title')
        self.assertEqual(my.filename, '')
        self.assertEqual(my.plaintext, 'Not so secret')
        self.assertEqual(my.ciphertext, '')

    def test_init_with_ct(self):
        my = Notes(title='my title', ciphertext='%% Very secret')
        self.assertEqual(my.title, 'my_title')
        self.assertEqual(my.filename, '')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '%% Very secret')

    def test_init_with_pt_file(self):
        my = Notes(title='my plain title', filename='my filename')
        self.assertEqual(my.title, 'my_plain_title')
        self.assertEqual(my.filename, 'my_filename')
        self.assertEqual(my._ftitle, 'my_filename')
        self.assertEqual(my._fext, '')

    def test_init_with_ct_file(self):
        my = Notes(title='my secret title', filename='encrypted filename.asc')
        self.assertEqual(my.title, 'my_secret_title')
        self.assertEqual(my.filename, 'encrypted_filename.asc')
        self.assertEqual(my._ftitle, 'encrypted_filename')
        self.assertEqual(my._fext, '.asc')

class TestNotesSetText(unittest.TestCase):
    def test_set_plaintext(self):
        my = Notes(title='this is my note title')
        self.assertEqual('this_is_my_note_title', my.title)
        self.assertEqual(my.filename, '')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '')
        my.set_plaintext('Hello World')
        self.assertEqual(my.plaintext, 'Hello World')
        self.assertEqual(my.ciphertext, '')

    def test_set_ciphertext(self):
        my = Notes(title='this is my note title')
        self.assertEqual('this_is_my_note_title', my.title)
        self.assertEqual(my.filename, '')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '')
        my.set_ciphertext('%% GI&THJhO&GyoIyuOBy')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '%% GI&THJhO&GyoIyuOBy')

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

class TestNoteSaveLoadNotes(unittest.TestCase):
    def test_save_ciphertext(self):
        n = Notes(title="testing CT save")
        n.set_ciphertext("%% GI&THJhO&GyoIyuOBy")
        n.save_ciphertext()
        self.assertTrue(os.path.exists(os.path.exists(get_note_fullpath("testing_CT_save.asc"))))

    def test_save_plaintext(self):
        n = Notes(title="testing PT save")
        n.set_plaintext("This is some text")
        n.save_plaintext()
        self.assertTrue(os.path.exists(get_note_fullpath("testing_PT_save")))

    def test_load_ciphertext(self):
        n1 = Notes(title="testing CT load")
        n1.set_ciphertext("%% GI&THJhO&GyoIyuOBy")
        n1.save_ciphertext()
        self.assertTrue(os.path.exists(get_note_fullpath("testing_CT_load.asc")))
        n2 = Notes(filename="testing_CT_load.asc")
        self.assertTrue(os.path.exists(get_note_fullpath("testing_CT_load.asc")))
        self.assertEqual(n1.ciphertext, n2.ciphertext)
        self.assertEqual(n1.plaintext, n2.plaintext)
        n3 = Notes()
        n3.filename="testing_CT_load.asc"
        n3.load_ciphertext()
        self.assertTrue(os.path.exists(get_note_fullpath("testing_CT_load.asc")))
        self.assertEqual(n1.ciphertext, n3.ciphertext)
        self.assertEqual(n1.plaintext, n3.plaintext)

    def test_load_plaintext(self):
        n1 = Notes(title="testing PT save")
        n1.set_plaintext("This is some text")
        n1.save_plaintext()
        self.assertTrue(os.path.exists(get_note_fullpath("testing_PT_save")))
        n2 = Notes()

    def test_import_note(self):     # imports a note from full pathname file
        n = import_note('/etc/motd')
        self.assertNotEqual(n.plaintext, "")
        self.assertEqual(n.ciphertext, "")

class TestNoteFileFunctions(unittest.TestCase):
    def test_rename_note(self):
        pass


if __name__ == "__main__":
    unittest.main()
