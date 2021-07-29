# TESTING NOTEBOOKS

import unittest
import os
import shutil
from pynoteslib import Notebook, Config, Notesystem


class TestNotebooks(unittest.TestCase):
    def setUp(self):
        self.ns = Notesystem()
        self.nb = Notebook()

    def test_init(self):
        self.assertTrue(self.nb.testinit)

    def test_notebook_create(self):
        self.assertTrue(self.nb.create('notebook Create'))
        self.assertTrue(os.path.exists(self.nb.notebookpath))

    def test_notebook_rename(self):
        newname = 'After rename'
        self.nb.create('Before rename')
        self.nb.rename(newname)
        self.assertTrue(os.path.exists(self.nb.notebookpath))
        self.assertFalse(os.path.exists(self.nb.config.usenotebook + newname))    

    def test_get_notebooks(self):
        try:
            shutil.rmtree(self.ns.config.notesdir + '/Another_notebook')
        except:
            pass
        r = self.ns.get_notebooks()
        self.nb.create('Another notebook')
        self.assertEqual(self.ns.get_notebooks(), r + ['Another_notebook'])

    def test_delete_notebook(self):
        todel = 'notebook_to_delete'
        self.nb.create(todel)
        self.assertTrue(os.path.exists(self.nb.notebookpath))
        shutil.rmtree(self.nb.notebookpath)
        self.assertFalse(os.path.exists(self.nb.notebookpath))

    def test_duplicate_otebook(self):
        self.assertTrue(self.nb.create('notebook to copy'))
        self.assertTrue(os.path.exists(self.nb.notebookpath))
        self.nb.duplicate('notebook copied')
        self.assertTrue(os.path.exists(self.ns.config.notesdir + '/notebook_copied'))     
    
    def test_default(self):
        self.nb.create('move_from_default')
        self.nb.use('move_from_default')
        self.assertEqual(self.nb.config.usenotebook, 'move_from_default')
        self.nb.default()
        self.assertEqual(self.nb.config.usenotebook, self.nb.config.defaultnotebook)

    def test_use(self):
        self.nb.create('one')
        self.nb.create('two')
        self.nb.use('one')
        self.assertEqual(self.nb.config.usenotebook, 'one')
        self.nb.use('two')
        self.assertEqual(self.nb.config.usenotebook, 'two')
        self.nb.use('one')
        self.assertEqual(self.nb.config.usenotebook, 'one')

if __name__ == "__main__":
    unittest.main()