
# TESTING NOTES

import unittest, os, shutil, pathlib
from dumper import dump
from pynotes import notes, notebook, config, notesystem

class TestNotes(unittest.TestCase):
    def setUp(self):
        self.n = notes()
        self.nb = notebook()

    def test_init(self):
        self.assertTrue(self.n.testinit)

    def test_createnote(self):
        self.n.create("testing create note")

    def test_setPlaintext(self):
        self.n.create("testing CT")
        self.n.setPlaintext('This is some text')
        self.assertEqual(self.n.plaintext, 'This is some text')

    def test_setCiphertext(self):
        self.n.create("testing PT")
        self.n.setCiphertext('GI&THJhO&GyoIyuOBy')
        self.assertEqual(self.n.ciphertext, 'GI&THJhO&GyoIyuOBy')

    def test_saveCiphertext(self):
        self.n.create("testing CT save")
        self.n.setCiphertext('GI&THJhO&GyoIyuOBy')
        self.n.saveCiphertext()
        self.assertTrue(os.path.exists(self.n.prependUseNotebook('testing_CT_save.asc')))

    def test_savePlaintext(self):
        self.n.create("testing PT save")
        self.n.setPlaintext('This is some text')
        self.n.savePlaintext()
        self.assertTrue(os.path.exists(self.n.prependUseNotebook('testing_PT_save')))

    def test_encrypt(self):
        self.n.create("testing encrypt")
        self.n.setPlaintext('This is some text')
        self.n.encrypt()
        self.n.saveCiphertext()
        self.assertTrue(os.path.exists(self.n.prependUseNotebook('testing_encrypt.asc')))

    def test_decrypt(self):
        self.n.create("testing decrypt")
        self.n.setCiphertext('%% This is some text')
        self.n.decrypt()
        self.n.savePlaintext()
        self.assertTrue(os.path.exists(self.n.prependUseNotebook('testing_decrypt')))

    def test_prependUseNotebook(self):
        testpath = self.n.prependUseNotebook('demo.txt')
        self.assertEqual(testpath[-35::], '__testing__/notesdir/Notes/demo.txt')

    def test_prependAnotebook(self):
        testpath = self.n.prependAnotebook('Other', 'demo.txt')
        self.assertEqual(testpath[-35::], '__testing__/notesdir/Other/demo.txt')

    def test_importNote(self):
        self.n.plaintext = ''
        self.n.importNote('LICENCE')
        self.assertNotEqual(self.n.plaintext, '')

    def test_renamenote(self):
        self.n.create("before_rename_note")
        self.n.savePlaintext()
        self.n.rename("after rename")
        self.assertTrue(os.path.exists(self.n.prependUseNotebook('after_rename')))
        self.assertFalse(os.path.exists(self.n.prependUseNotebook('before_rename_note')))

    def test_duplicatenote(self):
        self.n.create("before_dup_note")
        self.n.savePlaintext()
        self.n.duplicate("after dup note")
        self.n.savePlaintext()
        self.assertTrue(os.path.exists(self.n.prependUseNotebook('after_dup_note')))
        self.assertTrue(os.path.exists(self.n.prependUseNotebook('before_dup_note')))

    def test_moveTo(self):
        self.nb.create('Other')
        self.n.create("moveTo test")
        self.n.savePlaintext()
        self.assertTrue(os.path.exists(self.n.prependUseNotebook('moveTo_test')))
        self.n.moveTo('Other')
        self.assertTrue(os.path.exists(self.n.prependAnotebook('Other', 'moveTo_test')))
        self.assertFalse(os.path.exists(self.n.prependUseNotebook('moveTo_test')))

    def test_copyTo(self):
        self.nb.create('Other')
        self.n.create("copyTo test")
        self.n.savePlaintext()
        self.assertTrue(os.path.exists(self.n.prependUseNotebook('copyTo_test')))
        self.n.copyTo('Other')
        self.assertTrue(os.path.exists(self.n.prependAnotebook('Other','copyTo_test')))
        self.assertTrue(os.path.exists(self.n.prependUseNotebook('copyTo_test')))

    def test_openNote(self):
##        import pudb; pudb.set_trace()
        self.n.create('Testing Open Note')
        self.n.setPlaintext('This is some text\nThis is more text of the file')
        self.n.encrypt()

        self.n.saveCiphertext()
        self.assertTrue(os.path.exists(self.n.prependUseNotebook('Testing_Open_Note.asc')))

        op = notes()
        op.open('Testing_Open_Note.asc')
        self.assertEqual(op.notetitle, 'Testing_Open_Note')

        op.decrypt()
        self.assertEqual(op.plaintext, 'This is some text\nThis is more text of the file')

if __name__ == "__main__":
    unittest.main()

