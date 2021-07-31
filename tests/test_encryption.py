import unittest
import pynoteslib as nl

class MyTestCase(unittest.TestCase):
    def test_encryption(self):
        pt = 'Hello World'
        self.assertEqual(nl.encrypt(pt), '%% ' + pt)

    def test_decryption(self):
        ct = '%% Hello World'
        self.assertEqual(nl.decrypt(ct), ct[3:])

# if __name__ == '__main__':
#     unittest.main()
