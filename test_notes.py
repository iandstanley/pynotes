
# TESTING CONFIG

import unittest
from pynotes import notes

class TestConfig(unittest.TestCase):
    def test_init(self):
            n = notes()
            self.assertTrue(n.testinit)
