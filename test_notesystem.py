
# TESTING NOTESYSTEM

import os
import unittest
from pynotes import config, notesystem
import dumper

class TestNotesystem(unittest.TestCase):
    ''' Testing notesystem without GIT
    '''
    def setUp(self):
        self.n = notesystem()
        
    def test_init_no_git(self):
        self.assertTrue(self.n.initran)
        self.assertTrue(self.n.config.initran)
        self.assertNotEqual(self.n.config.gpgkey, "DummyGpgKey")
        # Check all directories are created
        self.assertTrue(os.path.isdir(self.n.config.notesdir))
        self.assertTrue(os.path.isdir(self.n.default_fullpath))
        self.assertTrue(os.path.isdir(self.n.use_fullpath))
    
    def test_getDefaultNotebook(self):
        self.assertEqual(self.n.getDefaultNotebook(), "Notes")

    def test_getDefaultNotebookFullpath(self):
        self.assertEqual(self.n.getDefaultNotebookFullpath(), self.n.config.notesdir + '/'  + "Notes")

    def test_getUseNotebook(self):
        self.assertEqual(self.n.getUseNotebook(), "Notes")

    def test_getUseNotebookFullpath(self):
        self.assertEqual(self.n.getUseNotebookFullpath(), self.n.config.notesdir + '/'  + "Notes")
        # Check all directories are created
        self.assertTrue(os.path.isdir(self.n.config.notesdir))
        self.assertTrue(os.path.isdir(self.n.default_fullpath))
        self.assertTrue(os.path.isdir(self.n.use_fullpath))
        
    def test_getDefaultNotebook(self):
        self.assertEqual(self.n.getDefaultNotebook(), "Notes")

    def test_getDefaultNotebookFullpath(self):
        self.assertEqual(self.n.getDefaultNotebookFullpath(), self.n.config.notesdir + '/'  + "Notes")

    def test_getUseNotebook(self):
        self.assertEqual(self.n.getUseNotebook(), "Notes")

    def test_getUseNotebookFullpath(self):
        self.assertTrue(self.n.backup())

    def test_validGPGkey(self):
        self.assertTrue(self.n.validateGPGkey('C7E223E0361DF63A'))  # VALID PRIVATE KEY

    def test_invalidGPGkey(self):
        self.assertFalse(self.n.validateGPGkey('ABCDEF'))  # INVALID DUMMY KEY
        self.assertFalse(self.n.validateGPGkey('AC530D520F2F3269F5E98313A48449044AAD5C5D'))  # VALID LONG PUBLIC KEY
        self.assertFalse(self.n.validateGPGkey('A48449044AAD5C5D'))  # VALID SHORT PUBLIC KEY
   
    def test_newkey(self):
        self.assertTrue(self.n.newKey('C7E223E0361DF63A'))  # VALID PRIVATE KEY
        self.assertFalse(self.n.newKey('ABCDEF'))  # INVALID DUMMY KEY
        self.assertFalse(self.n.newKey('AC530D520F2F3269F5E98313A48449044AAD5C5D'))  # VALID LONG PUBLIC KEY
        self.assertFalse(self.n.newKey('A48449044AAD5C5D'))  # VALID SHORT PUBLIC KEY
          
    def test_backup(self):
        self.assertTrue(self.n.backup())
        # TODO: test tar error handling
        

class TestNotesystemWithGIT(unittest.TestCase):
    ''' Testing notesystem() with GIT
    '''
    def setUp(self):
        self.n = notesystem(git=True)
    
    def test_init_with_git(self):
        self.assertTrue(self.n.initran)
        self.assertTrue(self.n.config.initran)
        # Check all directories are created
        self.assertTrue(os.path.isdir(self.n.config.notesdir))
        self.assertTrue(os.path.isdir(self.n.default_fullpath))
        self.assertTrue(os.path.isdir(self.n.use_fullpath))
        # check notes system is configure for git
        c = config()
        c.readConfig()
        self.assertTrue(c.usegit)
        

