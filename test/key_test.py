import unittest

from entity.key import Key

class KeyTest(unittest.TestCase):

    def setUp(self):
        self.key = Key(bytes.fromhex("0123456789abcdef fedcba9876543210"))
        self.q_key_result = bytes.fromhex("6767313854966973 0857065648eabe43")

    def test_q_key(self):
        self.assertEqual(self.q_key_result, self.key.q_key())