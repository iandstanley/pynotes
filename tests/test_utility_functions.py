import os
import unittest
from dotenv import load_dotenv
load_dotenv(override=True)

# import pudb; pu.db

import pynoteslib as nl
#from pynoteslib import *

unittest.TestLoader.sortTestMethodsUsing = None


class TestUtilityFunctions(unittest.TestCase):

    def test_get_use_notebook(self):
        cf = nl.get_config()
        self.assertEqual(cf['use'],'Notes')
        self.assertEqual(cf['use'], nl.get_use_notebook())
        self.assertTrue(os.path.exists(nl.get_fullpath(cf['use'])))

    def test_get_default_notebook(self):
        cf = nl.get_config()
        self.assertEqual(cf['default'],'Notes')
        self.assertTrue(os.path.exists(nl.get_fullpath(cf['default'])))
        self.assertEqual(cf['default'], nl.get_default_notebook())
        self.assertTrue(os.path.exists(nl.get_fullpath(nl.get_default_notebook())))

    def test_use_notebook(self):
        cf = nl.get_config()
        self.assertEqual(cf['use'], nl.get_use_notebook())
        self.assertTrue(os.path.exists(nl.get_fullpath(cf['use'])))
        nl.create_notebook('testSetUseNB')
        self.assertTrue(os.path.exists(nl.get_fullpath('testSetUseNB')))
        nl.use_notebook('testSetUseNB')
        self.assertEqual(nl.get_use_notebook(), 'testSetUseNB')
        nl.use_notebook('Notes')
        self.assertEqual('Notes', nl.get_use_notebook())

    def test_default_notebook(self):
        cf = nl.get_config()
        self.assertEqual(cf['use'], nl.get_default_notebook())
        self.assertTrue(os.path.exists(nl.get_fullpath(cf['use'])))
        nl.create_notebook('testSetDefNB')
        self.assertTrue(os.path.exists(nl.get_fullpath('testSetDefNB')))
        nl.default_notebook('testSetDefNB')
        self.assertEqual(nl.get_default_notebook(), 'testSetDefNB')
        nl.default_notebook('Notes')
        self.assertEqual('Notes', nl.get_default_notebook())

    def test_get_notebooks(self):
        cf = nl.get_config()
        # create a new notebook, and check if 'Notes' and new notebook are in the returned list
        nl.create_notebook('testGetNB')
        self.assertTrue(os.path.exists(nl.get_fullpath('testGetNB')))
        self.assertNotEqual(set(['Notes', 'testGetNB']).intersection(nl.get_notebooks()), set())
