# TESTING CONFIG CLASS 

import unittest
from pynotes import Config, Notesystem


class TestConfig(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()