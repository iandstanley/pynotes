# TESTING CONFIG CLASS

import os
import unittest
# import pudb; pu.db

import pynoteslib as nl

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
    # def test_printenv(self):
    #     print('\nNOTESDIR = ' + os.environ["NOTESDIR"])
    #     print('HOME = ' + os.environ["HOME"])

    def test_read_default_config(self):
        c = nl._default_config
        self.assertEqual(nl._default_config, test_default_config_dict)

    def test_get_notesdir(self):
        self.assertEqual(nl.get_notesdir(), os.environ['HOME'] + "/pynotes/__testing__/.notes")

    def test_config_file(self):
        self.assertEqual(nl.get_config_file(), os.environ['HOME'] + "/pynotes/__testing__/.notes/config")

    def test_create_configfile(self):
        nl.create_config()
        self.assertTrue(os.path.exists(nl.get_config_file()))

    def test__write_config(self):
        conf = nl._default_config

    def test_get_config(self):
        r = nl.get_config()
        self.assertEqual(r['configfile'], os.environ["NOTESDIR"] + '/config' )

if __name__ == "__main__":
    unittest.main()
