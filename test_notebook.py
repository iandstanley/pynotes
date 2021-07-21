
# TESTING NOTEBOOKS

import unittest, os, shutil
from pynotes import notebook, config, notesystem

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.ns = notesystem()
        self.nb = notebook()

    def test_init(self):
        self.assertTrue(self.nb.testinit)

    def test_notebookCreate(self):
        self.assertTrue(self.nb.create('notebook Create'))
        self.assertTrue(os.path.exists(self.nb.notebookpath))

    def test_notebookRename(self):
        newname = 'After rename'
        self.nb.create('Before rename')
        self.nb.rename(newname)

    def test_getNotebooks(self):
        try:
            shutil.rmtree(self.ns.config.notesdir + '/Another_notebook')
        except:
            pass
        r = self.ns.getNotebooks()
        self.nb.create('Another notebook')
        self.assertEqual(self.ns.getNotebooks(),r + ['Another_notebook'])
