
# TESTING CONFIG

import unittest
from pynotes import config

class TestConfig(unittest.TestCase):
    def test_init(self):
            c = config()
            self.assertEqual(c.defaultnotebook,"Notes")
