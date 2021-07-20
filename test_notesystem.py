
# TESTING NOTESYSTEM

import unittest
from pynotes import *

class TestNotesystem(unittest.TestCase):
    def test_init(self):
        n = notesystem()
        self.assertTrue(n.initran)
        self.assertTrue(n.config.initran)


    def test_newkey(self):
        n = notesystem()
        self.assertTrue(n.newKey)


    def test_backup(self):
        n = notesystem()
        self.assertTrue(n.backup)



