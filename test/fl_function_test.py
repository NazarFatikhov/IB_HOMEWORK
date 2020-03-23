import unittest

from entity.fl_function import FLFunction

class FLFuncTest(unittest.TestCase):

    def setUp(self):
        self.x = bytes.fromhex("695e2dbc2a7211d1")
        self.key = bytes.fromhex("56e9afc745a49029")
        self.f_result = bytes.fromhex("86b8f745aae24ad9")
        self.y = bytes.fromhex("029d886d6c0dfb08")
        self.fl_inv_key = bytes.fromhex("e57e2495ab9c70f5")
        self.fl_inv_result = bytes.fromhex("ed007390a60dba29")

    def test_fl_func(self):
        self.assertEqual(FLFunction.fl_func(self.x, self.key), self.f_result)

    def test_fl_inv_func(self):
        self.assertEqual(FLFunction.fl_inv(self.y, self.fl_inv_key), self.fl_inv_result)