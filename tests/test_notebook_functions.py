
import os
import unittest
# import pudb; pu.db

import pynoteslib as nl
#from pynoteslib import *

unittest.TestLoader.sortTestMethodsUsing = None

test_default_config_dict = {
    "gpgkey": "",
    "spelling": "none",
    "default": "Notes",
    "use": "Notes",
    "home": "/home/ian",
    "notesdir": "",
    "configfile": "",
    "usegit": False
}


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



# if __name__ == "__main__":
#     unittest.main()
