import unittest

from entity.byte_sequence import ByteSequence


class ByteSequenceTest(unittest.TestCase):

    def setUp(self):
        self.bytes_ = bytes.fromhex("80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        self.left = bytes.fromhex("80 00 00 00 00 00 00 00")
        self.right = bytes.fromhex("00 00 00 00 00 00 00 00")
        self.byte_sequence = ByteSequence.from_bytes_string(bytes.fromhex("80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"))
        self.res_xor = bytes.fromhex("2D 9B A3 65 CC 4D D5 55 3D 2D 9F E3 03 84 1D 88")
        self.other_xor = bytes.fromhex("AD 9B A3 65 CC 4D D5 55 3D 2D 9F E3 03 84 1D 88")
        self.res_lor = bytes.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 40 00")
        self.count_lor = 15

    def test_get_L(self):
        self.assertEqual(self.left, self.byte_sequence.leftBytes)

    def test_get_R(self):
        self.assertEqual(self.right, self.byte_sequence.rightBytes)

    def test_get_Full(self):
        self.assertEqual(self.bytes_, self.byte_sequence.full_bytes(self.byte_sequence))

    def test_xor(self):
        res_byte_seq = self.byte_sequence.xor(self.byte_sequence, self.other_xor)
        self.assertEqual(self.res_xor.hex(), res_byte_seq.full_bytes(res_byte_seq).hex())

    def test_lor(self):
        res_byte_seq = self.byte_sequence.rol(self.byte_sequence, self.count_lor)
        self.assertEqual(self.res_lor, res_byte_seq.full_bytes(res_byte_seq))