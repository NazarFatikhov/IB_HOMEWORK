import unittest

from entity.key import Key

class KeyTest(unittest.TestCase):

    def setUp(self):
        self.key = bytes.fromhex("0123456789abcdef fedcba9876543210")
        self.q_key_result = bytes.fromhex("ae71c3d55ba6bf1d 169240a795f89256")

    def test_q_key(self):
        self.assertEqual(self.q_key_result, Key.q_key(self.key))