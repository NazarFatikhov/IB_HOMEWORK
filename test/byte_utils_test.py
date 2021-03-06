import unittest

from entity.byte_utils import ByteUtils


class ByteUtilsTest(unittest.TestCase):

    def setUp(self):
        self.bytes_ = bytes.fromhex("80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        self.left = bytes.fromhex("80 00 00 00 00 00 00 00")
        self.right = bytes.fromhex("00 00 00 00 00 00 00 00")
        self.res_xor = bytes.fromhex("2D 9B A3 65 CC 4D D5 55 3D 2D 9F E3 03 84 1D 88")
        self.other_xor = bytes.fromhex("AD 9B A3 65 CC 4D D5 55 3D 2D 9F E3 03 84 1D 88")
        self.res_rol = bytes.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 40 00")
        self.res_ror = bytes.fromhex("00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        self.count_rol = 15

    def test_get_L(self):
        self.assertEqual(self.left, ByteUtils.getLeftPart(self.bytes_))

    def test_get_R(self):
        self.assertEqual(self.right, ByteUtils.getRightPart(self.bytes_))

    def test_xor(self):
        self.assertEqual(self.res_xor.hex(), ByteUtils.xor(self.bytes_, self.other_xor).hex())

    def test_rol(self):
        self.assertEqual(self.res_rol, ByteUtils.rol(self.bytes_, self.count_rol))

    def test_ror(self):
        self.assertEqual(self.res_ror, ByteUtils.ror(self.bytes_, self.count_rol))