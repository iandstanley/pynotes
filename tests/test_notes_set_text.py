import unittest
import os
from pynoteslib import *
#import pynoteslib
#import pudb; pu.db


class Test_notes_set_text(unittest.TestCase):
    def test_set_plaintext(self):
        my = Notes(title='this is my note title')
        self.assertEqual('this_is_my_note_title', my.title)
        self.assertEqual(my.filename, 'this_is_my_note_title')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '')
        my.set_plaintext('Hello World')
        self.assertEqual(my.plaintext, 'Hello World')
        self.assertEqual(my.ciphertext, '')

    def test_set_ciphertext(self):
        my = Notes(title='this is my note title')
        self.assertEqual('this_is_my_note_title', my.title)
        self.assertEqual(my.filename, 'this_is_my_note_title')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '')
        my.set_ciphertext('%% GI&THJhO&GyoIyuOBy')
        self.assertEqual(my.filename, 'this_is_my_note_title.asc')
        self.assertEqual(my.plaintext, '')
        self.assertEqual(my.ciphertext, '%% GI&THJhO&GyoIyuOBy')
