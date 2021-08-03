import os
import unittest
#import pudb; pu.db

import pynoteslib as nl
#from pynoteslib import *

unittest.TestLoader.sortTestMethodsUsing = None

print(os.environ['NOTESDIR'] )
class TestPathFunctions(unittest.TestCase):

    def test_get_fullpath(self):
        self.assertEqual(os.environ['NOTESDIR'] + '/config', nl.get_fullpath('config'))

    def test_get_note_fullpath(self):
        self.assertEqual(os.environ['NOTESDIR'] + '/Notes/my_note', nl.get_note_fullpath('my_note'))

