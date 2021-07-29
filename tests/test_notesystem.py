# TESTING NOTESYSTEM

import unittest
import os
import gnupg
from pynoteslib import Config, Notesystem


class TestNotesystem(unittest.TestCase):
    """Testing notesystem without GIT"""

    def setUp(self):
        self.n = Notesystem()

    def test_init_no_git(self):
        self.assertTrue(self.n.initran)
        self.assertTrue(self.n.config.initran)
        self.assertNotEqual(self.n.config.gpgkey, "DummyGpgKey")
        # Check all directories are created
        self.assertTrue(os.path.isdir(self.n.config.notesdir))
        self.assertTrue(os.path.isdir(self.n.default_fullpath))
        self.assertTrue(os.path.isdir(self.n.use_fullpath))

    def test_get_default_notebook(self):
        self.assertEqual(self.n.get_default_notebook(), "Notes")

    def test_get_default_notebook_fullpath(self):
        self.assertEqual(
            self.n.get_default_notebook_fullpath(),
            self.n.config.notesdir + "/" + "Notes",
        )

    def test_get_use_notebook(self):
        self.assertEqual(self.n.get_use_notebook(), "Notes")

    def test_get_use_notebook_fullpath(self):
        self.assertEqual(
            self.n.get_use_notebook_fullpath(), self.n.config.notesdir + "/" + "Notes"
        )
        # Check all directories are created
        self.assertTrue(os.path.isdir(self.n.config.notesdir))
        self.assertTrue(os.path.isdir(self.n.default_fullpath))
        self.assertTrue(os.path.isdir(self.n.use_fullpath))

    def test_valid_gpg_key(self):
        self.assertTrue(
            self.n.validate_gpg_key("C7E223E0361DF63A")
        )  # VALID PRIVATE KEY

    def test_invalid_gpg_key(self):
        self.assertFalse(self.n.validate_gpg_key("ABCDEF"))  # INVALID DUMMY KEY
        self.assertFalse(
            self.n.validate_gpg_key("AC530D520F2F3269F5E98313A48449044AAD5C5D")
        )  # VALID LONG PUBLIC KEY
        self.assertFalse(
            self.n.validate_gpg_key("A48449044AAD5C5D")
        )  # VALID SHORT PUBLIC KEY

    def test_newkey(self):
        self.assertTrue(self.n.new_key("C7E223E0361DF63A"))  # VALID PRIVATE KEY
        self.assertFalse(self.n.new_key("ABCDEF"))  # INVALID DUMMY KEY
        self.assertFalse(
            self.n.new_key("AC530D520F2F3269F5E98313A48449044AAD5C5D")
        )  # VALID LONG PUBLIC KEY
        self.assertFalse(self.n.new_key("A48449044AAD5C5D"))  # VALID SHORT PUBLIC KEY

    def test_backup(self):
        self.assertTrue(self.n.backup())
        # TODO: test tar error handling


class TestNotesystemWithGIT(unittest.TestCase):
    """Testing notesystem() with GIT"""

    def setUp(self):
        self.n = Notesystem(git=True)

    def test_init_with_git(self):
        self.assertTrue(self.n.initran)
        self.assertTrue(self.n.config.initran)
        # Check all directories are created
        self.assertTrue(os.path.isdir(self.n.config.notesdir))
        self.assertTrue(os.path.isdir(self.n.default_fullpath))
        self.assertTrue(os.path.isdir(self.n.use_fullpath))
        # check notes system is configure for git
        c = Config()
        c.read_config()
        self.assertTrue(c.usegit)


if __name__ == "__main__":
    unittest.main()
