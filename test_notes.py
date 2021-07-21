
# TESTING NOTES

import unittest, os, shutil
from pynotes import notes, notebook, config, notesystem

class TestNotes(unittest.TestCase):
    def test_init(self):
        n = notes()
        self.assertTrue(n.testinit)
