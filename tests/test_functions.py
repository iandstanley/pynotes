
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


class TestFunctions(unittest.TestCase):
    # def test_printenv(self):
    #     print('\nNOTESDIR = ' + os.environ["NOTESDIR"])
    #     print('HOME = ' + os.environ["HOME"])

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

    def test_get_fullpath(self):
        self.assertEqual(os.environ['NOTESDIR'] + '/config', nl.get_fullpath('config'))

    def test_get_note_fullpath(self):
        self.assertEqual(os.environ['NOTESDIR'] + '/Notes/my_note', nl.get_note_fullpath('my_note'))

    def test_create_notebook(self):
        cf = nl.get_config()
        self.assertTrue(nl.create_notebook('testCreateNB'))

    def test_duplicate_notebook(self):
        cf = nl.get_config()
        self.assertTrue(nl.create_notebook('testdupone'))
        self.assertTrue(nl.duplicate_notebook('testdupone', 'testduptwo'))
        self.assertTrue(os.path.exists(nl.get_fullpath('testduptwo')))

    def test_rename_notebook(self):
        cf = nl.get_config()
        self.assertTrue(nl.create_notebook('testRenameOne'))
        self.assertTrue(os.path.exists(nl.get_fullpath('testRenameOne')))
        nl.rename_notebook('testRenameOne', 'testRenameTwo')
        self.assertTrue(os.path.exists(nl.get_fullpath('testRenameTwo')))

    def test_delete_notebook(self):
        cf = nl.get_config()
        self.assertTrue(nl.create_notebook('testDeleteNB'))
        self.assertTrue(os.path.exists(nl.get_fullpath('testDeleteNB')))
        self.assertTrue(nl.delete_notebook('testDeleteNB'))
        self.assertFalse(os.path.exists(nl.get_fullpath('testDeleteNB')))

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

    def test_get_use_notebook(self):
        cf = nl.get_config()
        self.assertEqual(cf['use'],'Notes')
        self.assertEqual(cf['use'], nl.get_use_notebook())
        self.assertTrue(os.path.exists(nl.get_fullpath(cf['use'])))

    def test_get_default_notebook(self):
        cf = nl.get_config()
        self.assertEqual(cf['default'],'Notes')
        self.assertTrue(os.path.exists(nl.get_fullpath(cf['default'])))
        self.assertEqual(cf['default'], nl.get_default_notebook())
        self.assertTrue(os.path.exists(nl.get_fullpath(nl.get_default_notebook())))

    def test_use_notebook(self):
        cf = nl.get_config()
        self.assertEqual(cf['use'], nl.get_use_notebook())
        self.assertTrue(os.path.exists(nl.get_fullpath(cf['use'])))
        nl.create_notebook('testSetUseNB')
        self.assertTrue(os.path.exists(nl.get_fullpath('testSetUseNB')))
        nl.use_notebook('testSetUseNB')
        self.assertEqual(nl.get_use_notebook(), 'testSetUseNB')
        nl.use_notebook('Notes')
        self.assertEqual('Notes', nl.get_use_notebook())

    def test_default_notebook(self):
        cf = nl.get_config()
        self.assertEqual(cf['use'], nl.get_default_notebook())
        self.assertTrue(os.path.exists(nl.get_fullpath(cf['use'])))
        nl.create_notebook('testSetDefNB')
        self.assertTrue(os.path.exists(nl.get_fullpath('testSetDefNB')))
        nl.default_notebook('testSetDefNB')
        self.assertEqual(nl.get_default_notebook(), 'testSetDefNB')
        nl.default_notebook('Notes')
        self.assertEqual('Notes', nl.get_default_notebook())

    def test_get_notebooks(self):
        cf = nl.get_config()
        # create a new notebook, and check if 'Notes' and new notebook are in the returned list
        nl.create_notebook('testGetNB')
        self.assertTrue(os.path.exists(nl.get_fullpath('testGetNB')))
        self.assertNotEqual(set(['Notes', 'testGetNB']).intersection(nl.get_notebooks()), set())


# if __name__ == "__main__":
#     unittest.main()
