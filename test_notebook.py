
# TESTING CONFIG

import unittest
from pynotes import notebook

class TestConfig(unittest.TestCase):
    def test_init(self):
            nb = notebook()
            self.assertTrue(nb.testinit)
