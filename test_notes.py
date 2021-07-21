
# TESTING NOTES

import unittest, os, shutil, pathlib
from pynotes import notes, notebook, config, notesystem

class TestNotes(unittest.TestCase):
    def setUp(self):
        self.n = notes()
        
    def test_init(self):
        self.assertTrue(self.n.testinit)

    def test_createnote(self):
        self.n.create("testing create note")
