import os
import unittest
from dotenv import load_dotenv
load_dotenv(override=True)
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


class TestConfigFunctions(unittest.TestCase):

    def test_read_default_config(self):
        c = nl._default_config
        self.assertEqual(nl._default_config, test_default_config_dict)

    def test_get_notesdir(self):
        self.assertEqual(nl.get_notesdir(), os.environ['NOTESDIR'])

    def test_config_file(self):
        self.assertEqual(nl.get_config_file(), os.environ['NOTESDIR'] + "/config")

    def test_create_configfile(self):
        nl.create_config()
        self.assertTrue(os.path.exists(nl.get_config_file()))

    def test__write_config(self):
        conf = nl._default_config

    def test_get_config(self):
        cf = nl.get_config()
        self.assertEqual(cf['configfile'], os.environ["NOTESDIR"] + '/config' )

    def test_use_git(self):
        conf = nl.get_config()
        self.assertEqual(conf['usegit'], nl.use_git())

    def test_set_git(self):
        conf = nl.get_config()
        self.assertEqual(conf['usegit'], nl.use_git())
        nl.set_git(True)
        conf = nl.get_config()
        self.assertEqual(conf['usegit'], True)
        nl.set_git(False)
        conf = nl.get_config()
        self.assertEqual(conf['usegit'], False)
        self.assertEqual(conf['usegit'], nl.use_git())
