
import unittest
import os

# from pynotes import Config, Notesystem
import pynoteslib as nl

# from pynoteslib import *

#breakpoint()
os.environ["NOTESDIR"] = "__testing__/.notes"
test_default_config_dict = {
    "gpgkey": "",
    "spelling": "none",
    "default": "Notes",
    "use": "Notes",
    "home": "/home/ian",
    "notesdir": "",
    "configfile": ""
}


class Testappdirs(unittest.TestCase):
    def test_init_dirs(self):
        breakpoint()
        conf = nl._default_config
        nl.init_dirs()
        nd = nl.get_notesdir()
        self.assertTrue(os.path.isdir(nd))
        #self.assertTrue(os.path.isdir(nd) + "/Notes")


if __name__ == "__main__":
    unittest.main()
