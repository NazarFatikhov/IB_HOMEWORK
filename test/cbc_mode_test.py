import unittest

from entity.cbc_mode import CBC

class CBCTest(unittest.TestCase):

    def setUp(self):
        self.key = bytes.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        self.x = bytes.fromhex("07 92 3A 39 EB 0A 81 7D 1C 4D 87 BD B8 2D 1F 1C 48 CD 64 19 80 96 72 D2 34 92 60 D8 9A 08")
        self.y = bytes.fromhex("07 92 3A 39 EB 0A 81 7D 1C 4D 87 BD B8 2D 1F 1C 48 CD 64 19 80 96 72 D2 34 92 60 D8 9A 08 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")

    def test_encrypt(self):
        result = CBC.encrypt(self.x, self.key)
        print(result)
        self.assertEqual(len(self.y), len(result))