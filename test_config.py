# TESTING CONFIG CLASS 

import unittest
from pynotes import config

class TestConfig(unittest.TestCase):
    def test_init(self):   
        c = config()
        self.assertTrue(c.initran)   # test __init__ runs to end

    def test_writeConfig(self):     
        c = config(git=True)
        c.writeConfig()             # write a configfile with usegit = True
        self.assertTrue(c.usegit)

        d = config()                
        d.readConfig()              # overwrite config with configfile
        self.assertTrue(d.usegit)

    def test_readConfig(self):      
        ng = config(git=False)      ## setup without git
        ng.writeConfig()
        c = config()
        c.readConfig()
        self.assertFalse(c.usegit)

        wg = config(git=True)       ## and without git
        wg.writeConfig()
        d = config()
        d.readConfig()
        self.assertTrue(d.usegit)
