# TESTING CONFIG CLASS 

import unittest, os, pathlib, shutil
from pynotes import config, notesystem

class TestConfig(unittest.TestCase):
    def test_init(self):
        n = notesystem()             # initialize notesystem as it will create NOTESDIR etc
        c = config()
        self.assertTrue(c.initran)   # test __init__ runs to end

    def test_writeConfig(self):     
        n = notesystem()             # initialize notesystem as it will create NOTESDIR etc

        c = config(git=True)
        c.setGPGkey(n.getDefaultGPGkey()) # fix up GPG key for tests (gets overwritten with second config() call
        c.writeConfig()             # write a configfile with usegit = True
        self.assertTrue(c.usegit)

        d = config()                
        d.readConfig()              # overwrite config with configfile
        self.assertTrue(d.usegit)

    def test_readConfig(self):      
        n = notesystem()             # initialize notesystem as it will create NOTESDIR etc

        ng = config(git=False)      # setup without git
        ng.setGPGkey(n.getDefaultGPGkey()) # fix up GPG key for tests (gets overwritten with second config() call
        ng.writeConfig()
        c = config()
        c.readConfig()
        self.assertFalse(c.usegit)

        wg = config(git=True)       # and without git
        wg.setGPGkey(n.getDefaultGPGkey()) # fix up GPG key for tests (gets overwritten with second config() call
        wg.writeConfig()
        d = config()
        d.readConfig()
        self.assertTrue(d.usegit)

    def test_setGPGkey(self):
        n = notesystem()             # initialize notesystem as it will create NOTESDIR etc
    
        n.config.gpgkey="REMOVED"   # manually set gpg key
        before = n.config.gpgkey
        n.config.setGPGkey(n.getDefaultGPGkey())    # reset to first private key on keyring
        after = n.config.gpgkey
        self.assertNotEqual(before, after)        
