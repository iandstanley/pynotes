import os
import unittest
from dotenv import load_dotenv
load_dotenv(override=True)

TESTKEY = 'E4D4E23B3AC48FFA15C1949216427604C30E9831'
#import pudb; pu.db

import pynoteslib as nl
#from pynoteslib import *

unittest.TestLoader.sortTestMethodsUsing = None


class TestNotefileFunctions(unittest.TestCase):

    def test_duplicate_notefile(self):
        cf = nl.get_config()
        cf['gpgkey'] = TESTKEY
        nl.write_config(cf)
        my = nl.Notes(title='before dup note', plaintext='Hello World')
        my.encrypt()
        my.save_ciphertext()
        self.assertTrue(os.path.exists(nl.get_note_fullpath(my.filename)))
        nl.duplicate_note('before dup note', 'after dup note')
        self.assertTrue(os.path.exists(nl.get_note_fullpath(my.filename)))
        self.assertTrue(os.path.exists(nl.get_note_fullpath('after_dup_note.asc')))


    def test_rename_notefile(self):
        cf = nl.get_config()
        cf['gpgkey'] = TESTKEY
        nl.write_config(cf)
        my = nl.Notes(title='before rename note', plaintext='Hello World')
        my.encrypt()
        my.save_ciphertext()
        self.assertTrue(os.path.exists(nl.get_note_fullpath(my.filename)))
        nl.rename_note('before_rename_note.asc', 'after rename note')
        self.assertTrue(os.path.exists(nl.get_note_fullpath('after_rename_note.asc')))


    def test_delete_notefile(self):
        cf = nl.get_config()
        cf['gpgkey'] = TESTKEY
        nl.write_config(cf)
        my = nl.Notes(title='delete note', plaintext='Hello World')
        my.encrypt()
        my.save_ciphertext()
        self.assertTrue(os.path.exists(nl.get_note_fullpath('delete_note.asc')))
        nl.delete_note('delete_note.asc')
        self.assertFalse(os.path.exists(nl.get_note_fullpath('delete_note.asc')))

    def test_copy_to_notebookfile(self):
        cf = nl.get_config()
        cf['gpgkey'] = TESTKEY
        nl.write_config(cf)
        my = nl.Notes(title='copyto note', plaintext='Hello World')
        my.encrypt()
        my.save_ciphertext()
        self.assertTrue(os.path.exists(nl.get_note_fullpath('copyto_note.asc')))
        self.assertTrue(nl.create_notebook('copy2notebook'))
        nl.copy_to_notebook(my.filename, 'copy2notebook')
        self.assertTrue(os.path.exists(nl.get_note_fullpath('copyto_note.asc')))
        self.assertTrue(os.path.exists(os.path.join(nl.get_notesdir(), 'copy2notebook' , 'copyto_note.asc')))

    def test_move_to_notebook(self):
        cf = nl.get_config()
        cf['gpgkey'] = TESTKEY
        nl.write_config(cf)
        my = nl.Notes(title='moveto note', plaintext='Hello World')
        my.encrypt()
        my.save_ciphertext()
        self.assertTrue(os.path.exists(nl.get_note_fullpath('moveto_note.asc')))
        self.assertTrue(nl.create_notebook('move2notebook'))
        nl.move_to_notebook(my.filename, 'move2notebook')
        self.assertFalse(os.path.exists(nl.get_note_fullpath('moveto_note.asc')))
        self.assertTrue(os.path.exists(os.path.join(nl.get_notesdir(), 'move2notebook' , 'moveto_note.asc')))
