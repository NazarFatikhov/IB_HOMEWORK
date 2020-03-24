import unittest

from entity.cameila import Camelia

class CameliaTest(unittest.TestCase):

    def setUp(self):
        self.key = bytes.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        self.x = bytes.fromhex("80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        self.y = bytes.fromhex("07 92 3A 39 EB 0A 81 7D 1C 4D 87 BD B8 2D 1F 1C")

    def test_encrypt(self):
        self.assertEqual(self.y, Camelia.encrypt(self.x, self.key))