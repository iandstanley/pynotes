
# TESTING NOTESYSTEM

import os
import unittest
from pynotes import config, notesystem
import dumper

class TestNotesystem(unittest.TestCase):
    def test_init_no_git(self):
        n = notesystem()
        self.assertTrue(n.initran)
        self.assertTrue(n.config.initran)

        # Check all directories are created
        self.assertTrue(os.path.isdir(n.config.notesdir))
        self.assertTrue(os.path.isdir(n.default_fullpath))
        self.assertTrue(os.path.isdir(n.use_fullpath))

    def test_init_with_git(self):
        n = notesystem(git=True)
        self.assertTrue(n.initran)
        self.assertTrue(n.config.initran)

        # Check all directories are created
        self.assertTrue(os.path.isdir(n.config.notesdir))
        self.assertTrue(os.path.isdir(n.default_fullpath))
        self.assertTrue(os.path.isdir(n.use_fullpath))

        # check notes system is configure for git
        c = config()
        c.readConfig()
        self.assertTrue(c.usegit)


    def test_getDefaultNotebook(self):
        n = notesystem()
        self.assertEqual(n.getDefaultNotebook(), "Notes")

    def test_getDefaultNotebookFullpath(self):
        n = notesystem()
        self.assertEqual(n.getDefaultNotebookFullpath(), n.config.notesdir + '/'  + "Notes")

    def test_getUseNotebook(self):
        n = notesystem()
        self.assertEqual(n.getUseNotebook(), "Notes")

    def test_getUseNotebookFullpath(self):
        n = notesystem()
        self.assertEqual(n.getUseNotebookFullpath(), n.config.notesdir + '/'  + "Notes")



        
##        dumper.dump(n)


##    def test_newkey(self):
##        n = notesystem()
##        self.assertTrue(n.newKey)
##
##
##    def test_backup(self):
##        n = notesystem()
##        self.assertTrue(n.backup)



