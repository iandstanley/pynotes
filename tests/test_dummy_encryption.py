import unittest
import pynoteslib as nl

class Test_dummy_encryption(unittest.TestCase):
    def test_encryption(self):
        pt = 'Hello World'
        self.assertEqual(nl.encrypt(pt), '%% ' + pt)

    def test_decryption(self):
        ct = '%% Hello World'
        self.assertEqual(nl.decrypt(ct), ct[3:])
