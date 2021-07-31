# TESTING NOTES

import unittest
import os
#from pynoteslib import Notes
import pynoteslib
#exit()

class TestNotes(unittest.TestCase):
    def test_nothing(self):
        pass
    '''
    def setUp(self):
        self.n = Notes()
        self.nb = Notebook()

    def test_init(self):
        self.assertTrue(self.n.testinit)

    def test_create_note(self):
        self.n.create("testing create note")

    def test_set_plaintext(self):
        self.n.create("testing CT")
        self.n.set_plaintext("This is some text")
        self.assertEqual(self.n.plaintext, "This is some text")

    def test_set_ciphertext(self):
        self.n.create("testing PT")
        self.n.set_ciphertext("GI&THJhO&GyoIyuOBy")
        self.assertEqual(self.n.ciphertext, "GI&THJhO&GyoIyuOBy")

    def test_save_ciphertext(self):
        self.n.create("testing CT save")
        self.n.set_ciphertext("GI&THJhO&GyoIyuOBy")
        self.n.save_ciphertext()
        self.assertTrue(
            os.path.exists(self.n.prepend_use_notebook("testing_CT_save.asc"))
        )

    def test_save_plaintext(self):
        self.n.create("testing PT save")
        self.n.set_plaintext("This is some text")
        self.n.save_plaintext()
        self.assertTrue(os.path.exists(self.n.prepend_use_notebook("testing_PT_save")))

    def test_encrypt(self):
        self.n.create("testing encrypt")
        self.n.set_plaintext("This is some text")
        self.n.encrypt()
        self.n.save_ciphertext()
        self.assertTrue(
            os.path.exists(self.n.prepend_use_notebook("testing_encrypt.asc"))
        )

    def test_decrypt(self):
        self.n.create("testing decrypt")
        self.n.set_ciphertext("%% This is some text")
        self.n.decrypt()
        self.n.save_plaintext()
        self.assertTrue(os.path.exists(self.n.prepend_use_notebook("testing_decrypt")))

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

# if __name__ == "__main__":
#     unittest.main()
