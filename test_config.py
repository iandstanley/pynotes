# TESTING CONFIG CLASS

import os
import unittest
unittest.TestLoader.sortTestMethodsUsing = None


# from pynotes import Config, Notesystem
import pynoteslib as nl

# from pynoteslib import *

os.environ["NOTESDIR"] = os.environ['HOME'] + "/pynotes/__testing__/.notes"
test_default_config_dict = {
    "gpgkey": "",
    "spelling": "none",
    "default": "Notes",
    "use": "Notes",
    "home": "/home/ian",
    "notesdir": "",
    "configfile": ""
}


class TestConfigFunctions(unittest.TestCase):
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

"""
    def test_init(self):
        n = Notesystem()             # initialize notesystem as it will create NOTESDIR etc
        c = Config()
        self.assertTrue(c.initran)   # test __init__ runs to end

    def test_write_config(self):
        n = Notesystem()             # initialize notesystem as it will create NOTESDIR etc

        c = Config(git=True)
        c.set_gpg_key(n.get_default_gpg_key())   # fix up GPG key for tests (gets overwritten with second config() call
        c.write_config()             # write a configfile with usegit = True
        self.assertTrue(c.usegit)

        d = Config()
        d.read_config()              # overwrite config with configfile
        self.assertTrue(d.usegit)

    def test_read_config(self):
        n = Notesystem()             # initialize notesystem as it will create NOTESDIR etc

        ng = Config(git=False)      # setup without git
        ng.set_gpg_key(n.get_default_gpg_key())  # fix up GPG key for tests (gets overwritten with second config() call
        ng.write_config()
        c = Config()
        c.read_config()
        self.assertFalse(c.usegit)

        wg = Config(git=True)       # and without git
        wg.set_gpg_key(n.get_default_gpg_key())  # fix up GPG key for tests (gets overwritten with second config() call
        wg.write_config()
        d = Config()
        d.read_config()
        self.assertTrue(d.usegit)

    def test_set_gpg_key(self):
        n = Notesystem()             # initialize notesystem as it will create NOTESDIR etc
    
        n.config.gpgkey = "REMOVED"   # manually set gpg key
        before = n.config.gpgkey
        n.config.set_gpg_key(n.get_default_gpg_key())    # reset to first private key on keyring
        after = n.config.gpgkey
        self.assertNotEqual(before, after)        
"""

if __name__ == "__main__":
    unittest.main()
