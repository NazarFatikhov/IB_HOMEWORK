import unittest

from entity.f_function import FFunc

class FFuncTest(unittest.TestCase):

    def setUp(self):
        self.x = bytes.fromhex("029d886d6c0dfb08")
        self.key = bytes.fromhex("2053cafc492b5738")
        self.f_result = bytes.fromhex("f38f754458e23ccf")

    def test_f_func(self):
        self.assertEqual(FFunc.f_func(self.x, self.key), self.f_result)

    def test_s1(self):
        self.assertEqual(bytes.fromhex("EC"), FFunc.s1(bytes.fromhex("03")))

    def test_s2(self):
        self.assertEqual(bytes.fromhex("D9"), FFunc.s2(bytes.fromhex("03")))

    def test_s3(self):
        self.assertEqual(bytes.fromhex("76"), FFunc.s3(bytes.fromhex("03")))

    def test_s4(self):
        self.assertEqual(bytes.fromhex("C0"), FFunc.s4(bytes.fromhex("03")))