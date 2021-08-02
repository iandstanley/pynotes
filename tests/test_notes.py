# TESTING NOTES

import unittest
import os
from pynoteslib import *
#import pynoteslib


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
        self.assertEqual(my.ftitle, 'my_filename')
        self.assertEqual(my.fext, '')

    def test_init_with_ct_file(self):
        my = Notes(title='my secret title', filename='encrypted filename.asc')
        self.assertEqual(my.title, 'my_secret_title')
        self.assertEqual(my.filename, 'encrypted_filename.asc')
        self.assertEqual(my.ftitle, 'encrypted_filename')
        self.assertEqual(my.fext, '.asc')

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
        self.assertTrue(
            os.path.exists(os.path.exists(get_note_fullpath("testing_CT_save.asc")))
        )

    def test_save_plaintext(self):
        n = Notes(title="testing PT save")
        n.set_plaintext("This is some text")
        n.save_plaintext()
        self.assertTrue(os.path.exists(get_note_fullpath("testing_PT_save")))

    '''

    def test_prepend_use_notebook(self):
        testpath = self.n.prepend_use_notebook("demo.txt")
        self.assertEqual(testpath[-35::], "__testing__/notesdir/Notes/demo.txt")

    def test_prepend_a_notebook(self):
        testpath = self.n.prepend_a_notebook("Other", "demo.txt")
        self.assertEqual(testpath[-35::], "__testing__/notesdir/Other/demo.txt")

    def test_import_note(self):
        self.n.plaintext = ""
        self.n.import_note("LICENCE")
        self.assertNotEqual(self.n.plaintext, "")

    def test_rename_note(self):
        self.n.create("before_rename_note")
        self.n.save_plaintext()
        self.n.rename("after rename")
        self.assertTrue(os.path.exists(self.n.prepend_use_notebook("after_rename")))
        self.assertFalse(
            os.path.exists(self.n.prepend_use_notebook("before_rename_note"))
        )

    def test_duplicate_note(self):
        self.n.create("before_dup_note")
        self.n.save_plaintext()
        self.n.duplicate("after dup note")
        self.n.save_plaintext()
        self.assertTrue(os.path.exists(self.n.prepend_use_notebook("after_dup_note")))
        self.assertTrue(os.path.exists(self.n.prepend_use_notebook("before_dup_note")))

    def test_move_to(self):
        self.nb.create("Other")
        self.n.create("moveTo test")
        self.n.save_plaintext()
        self.assertTrue(os.path.exists(self.n.prepend_use_notebook("moveTo_test")))
        self.n.move_to("Other")
        self.assertTrue(
            os.path.exists(self.n.prepend_a_notebook("Other", "moveTo_test"))
        )
        self.assertFalse(os.path.exists(self.n.prepend_use_notebook("moveTo_test")))

    def test_copy_to(self):
        self.nb.create("Other")
        self.n.create("copyTo test")
        self.n.save_plaintext()
        self.assertTrue(os.path.exists(self.n.prepend_use_notebook("copyTo_test")))
        self.n.copy_to("Other")
        self.assertTrue(
            os.path.exists(self.n.prepend_a_notebook("Other", "copyTo_test"))
        )
        self.assertTrue(os.path.exists(self.n.prepend_use_notebook("copyTo_test")))

    def test_open_note(self):
        self.n.create("Testing Open Note")
        self.n.set_plaintext("This is some text\nThis is more text of the file")
        self.n.encrypt()

        self.n.save_ciphertext()
        self.assertTrue(
            os.path.exists(self.n.prepend_use_notebook("Testing_Open_Note.asc"))
        )

        op = Notes()
        op.open("Testing_Open_Note.asc")
        self.assertEqual(op.notetitle, "Testing_Open_Note")

        op.decrypt()
        self.assertEqual(
            op.plaintext, "This is some text\nThis is more text of the file"
        )
    '''

if __name__ == "__main__":
    unittest.main()
