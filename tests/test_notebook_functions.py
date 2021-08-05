import os
import unittest
from dotenv import load_dotenv
load_dotenv(override=True)

# import pudb; pu.db

import pynoteslib as nl
#from pynoteslib import *

unittest.TestLoader.sortTestMethodsUsing = None


class TestNotebookFunctions(unittest.TestCase):

    def test_create_notebook(self):
        cf = nl.get_config()
        self.assertTrue(nl.create_notebook('testCreateNB'))

    def test_duplicate_notebook(self):
        cf = nl.get_config()
        self.assertTrue(nl.create_notebook('testdupone'))
        self.assertTrue(nl.duplicate_notebook('testdupone', 'testduptwo'))
        self.assertTrue(os.path.exists(nl.get_fullpath('testduptwo')))

    def test_rename_notebook(self):
        cf = nl.get_config()
        self.assertTrue(nl.create_notebook('testRenameOne'))
        self.assertTrue(os.path.exists(nl.get_fullpath('testRenameOne')))
        nl.rename_notebook('testRenameOne', 'testRenameTwo')
        self.assertTrue(os.path.exists(nl.get_fullpath('testRenameTwo')))

    def test_delete_notebook(self):
        cf = nl.get_config()
        self.assertTrue(nl.create_notebook('testDeleteNB'))
        self.assertTrue(os.path.exists(nl.get_fullpath('testDeleteNB')))
        self.assertTrue(nl.delete_notebook('testDeleteNB'))
        self.assertFalse(os.path.exists(nl.get_fullpath('testDeleteNB')))

    def test_get_notes_from_notebook(self):
        cf = nl.get_config()
        self.assertTrue(nl.create_notebook('testgetnotesNB'))
        nl.use_notebook('testgetnotesNB')
        n1 = nl.Notes(title='note1', plaintext='Hello World')
        n1.encrypt()
        n1.save_ciphertext()
        self.assertTrue(os.path.exists(os.path.join(nl.get_notesdir(), 'testgetnotesNB', n1.filename )))
        n2 = nl.Notes(title='note2', plaintext='Hello World')
        n2.encrypt()
        n2.save_ciphertext()
        self.assertTrue(os.path.exists(os.path.join(nl.get_notesdir(), 'testgetnotesNB', n2.filename )))
        notelist = nl.get_notes('testgetnotesNB')
        self.assertEqual(notelist.sort(), ['note1.asc', 'note2.asc'].sort())
        nl.use_notebook('Notes')

