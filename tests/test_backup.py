import unittest
import os
import datetime
from dotenv import load_dotenv
load_dotenv(override=True)
from pynoteslib import *
#import pynoteslib
#import pudb; pu.db


class TestBackupToTar(unittest.TestCase):
    def test_backup(self):
        cf = get_config()
        t = datetime.datetime.now()
        #conf = get_config()
        tarfile = (
            f"../notes_backup_{t.strftime('%Y%b%d_%H%M')}.tar"
        )
        result, tf = backup(cf)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(tf))
	
