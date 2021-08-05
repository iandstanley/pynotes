import unittest
import os
from dotenv import load_dotenv
load_dotenv(override=True)

from pynoteslib import *

#import pynoteslib
#import pudb; pu.db


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
