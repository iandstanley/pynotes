
# TESTING NOTES

import unittest, os, shutil, pathlib
from dumper import dump
from pynotes import notes, notebook, config, notesystem

class TestNotes(unittest.TestCase):
    def setUp(self):
        self.n = notes()
        
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

    def test_savePlaintext(self):
        self.n.create("testing PT save")
        self.n.setPlaintext('This is some text')
        self.n.savePlaintext()


    def test_prependNotebook(self):
        testpath = self.n.prependNotebook('demo.txt')
        self.assertEqual(testpath, '__testing__/notesdir/Notes/demo.txt')

    def test_importNote(self):
        self.n.plaintext = ''
        self.n.importNote('LICENCE')
        self.assertNotEqual(self.n.plaintext, '')
