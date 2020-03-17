import unittest

from entity.key import Key

class KeyTest(unittest.TestCase):

    def setUp(self):
        self.key = Key(bytes.fromhex("0123456789abcdeffedcba9876543210"))
        self.q_key_result = bytes.fromhex("20 9e 66 7f 3b cc 90 8b")

    def test_q_key(self):
        self.assertEqual(self.q_key_result, self.key.q_key())