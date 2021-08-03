import unittest
import os
from pynoteslib import *
#import pynoteslib
#import pudb; pu.db

class TestNotesClassInitiators(unittest.TestCase):
    def test_nothing(self):
        pass

    def test_init(self):
        my = Notes()
        self.assertTrue(my.testinit)
        self.assertEqual(my.title, '')
        self.assertEqual(my.filename, '')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '')

    def test_init_with_title(self):
        my = Notes(title='this is my note title')
        self.assertEqual('this_is_my_note_title', my.title)
        self.assertEqual(my.filename, '')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '')

    def test_init_with_pt(self):
        my = Notes(title='my title', plaintext='Not so secret')
        self.assertEqual(my.title, 'my_title')
        self.assertEqual(my.filename, '')
        self.assertEqual(my.plaintext, 'Not so secret')
        self.assertEqual(my.ciphertext, '')

    def test_init_with_ct(self):
        my = Notes(title='my title', ciphertext='%% Very secret')
        self.assertEqual(my.title, 'my_title')
        self.assertEqual(my.filename, '')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '%% Very secret')

    def test_init_with_pt_file(self):
        my = Notes(title='my plain title', filename='my filename')
        self.assertEqual(my.title, 'my_plain_title')
        self.assertEqual(my.filename, 'my_filename')
        self.assertEqual(my._ftitle, 'my_filename')
        self.assertEqual(my._fext, '')

    def test_init_with_ct_file(self):
        my = Notes(title='my secret title', filename='encrypted filename.asc')
        self.assertEqual(my.title, 'my_secret_title')
        self.assertEqual(my.filename, 'encrypted_filename.asc')
        self.assertEqual(my._ftitle, 'encrypted_filename')
        self.assertEqual(my._fext, '.asc')
