
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


class TestNotefileFunctions(unittest.TestCase):

    # def test_duplicate_notefile(self):
    #     cf = nl.get_config()
    #     my = nl.Notes(title='before dup note', plaintext='Hello World')
    #     my.encrypt()
    #     print(my.plaintext)
    #     print(my.filename)
    #     my.save_ciphertext()
    #     self.assertTrue(os.path.exists(nl.get_note_fullpath(my.filename)))

    def test_rename_notefile(self):
        cf = nl.get_config()
        my = nl.Notes(title='before rename note', plaintext='Hello World')
        my.encrypt()
        print(my.plaintext)
        print(my.filename)
        my.save_ciphertext()
        self.assertTrue(os.path.exists(nl.get_note_fullpath(my.filename)))
        nl.rename_note('before_rename_note.asc', 'after rename notemake tree')
        self.assertTrue(os.path.exists(nl.get_note_fullpath('after_rename_note.asc')))


    # def test_delete_notefile(self):
    #     cf = nl.get_config()
    #     self.assertTrue(nl.create_notebook('testDeleteNB'))
    #     self.assertTrue(os.path.exists(nl.get_fullpath('testDeleteNB')))
    #     self.assertTrue(nl.delete_notebook('testDeleteNB'))
    #     self.assertFalse(os.path.exists(nl.get_fullpath('testDeleteNB')))

    # def test_copy_to_notebookfile(self):
    #     cf = nl.get_config()
    #     self.assertTrue(nl.create_notebook('testRenameOne'))
    #     self.assertTrue(os.path.exists(nl.get_fullpath('testRenameOne')))
    #     nl.rename_notebook('testRenameOne', 'testRenameTwo')
    #     self.assertTrue(os.path.exists(nl.get_fullpath('testRenameTwo')))

    # def test_move_to_notebook(self):
    #     cf = nl.get_config()
    #     self.assertTrue(nl.create_notebook('testDeleteNB'))
    #     self.assertTrue(os.path.exists(nl.get_fullpath('testDeleteNB')))
    #     self.assertTrue(nl.delete_notebook('testDeleteNB'))
    #     self.assertFalse(os.path.exists(nl.get_fullpath('testDeleteNB')))



# if __name__ == "__main__":
#     unittest.main()
