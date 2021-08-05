import unittest
import os
from dotenv import load_dotenv
load_dotenv(override=True)
from pynoteslib import *
#import pynoteslib
#import pudb; pu.db


class TestDotEnv(unittest.TestCase):
    def test_env(self):
        """NOTESDIR=/home/ian/pynotes/__testing__/notesdir"""
        #print(f"NOTESDIR ==> ", os.getenv('NOTESDIR'))
        self.assertEqual("/home/ian/pynotes/__testing__/notesdir", os.getenv('NOTESDIR'))

