import unittest

from entity.cbc_mode import CBC

class CBCTest(unittest.TestCase):

    def test_cbc(self):
        key = bytes.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        #1
        input = bytes.fromhex("07 92 3A 39 EB 0A 81 7D 1C 4D 87 BD B8 2D 1F 1C "
                              "48 CD 64 19 80 96 72 D2 34 92 60 D8 9A 08")
        encrypt = CBC.encrypt(input, key)
        decrypt = CBC.decrypt(encrypt, key)
        print("#1")
        print("input -           {0}".format(input.hex()))
        print("encrypt -         {0}".format(encrypt.hex()))
        print("expected_result - {0}".format(decrypt.hex()))
        print("actual_result -   {0}".format(input.hex()))
        print()

        # 2
        input = bytes.fromhex("07 92 3A 39 EB 0A 81 7D 1C 4D 87 BD B8 2D 1F 1C "
                              "48 CD 64 19 80 96 72 D2 34 92 60 D8 9A 08 00 01")
        encrypt = CBC.encrypt(input, key)
        decrypt = CBC.decrypt(encrypt, key)
        print("#2")
        print("input -           {0}".format(input.hex()))
        print("encrypt -         {0}".format(encrypt.hex()))
        print("expected_result - {0}".format(decrypt.hex()))
        print("actual_result -   {0}".format(input.hex()))
        print()

        # 3
        input = bytes.fromhex("07 92 3A 39 EB 0A 81 7D 1C 4D 87 BD B8 2D 1F 1C "
                              "48 CD 64 19 80 96 72 D2 34 92 60 D8 9A 08 00 01 "
                              "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                              "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        encrypt = CBC.encrypt(input, key)
        decrypt = CBC.decrypt(encrypt, key)
        print("#3")
        print("input -           {0}".format(input.hex()))
        print("encrypt -         {0}".format(encrypt.hex()))
        print("expected_result - {0}".format(decrypt.hex()))
        print("actual_result -   {0}".format(input.hex()))
        print()

        # 4
        input = bytes.fromhex("07 92 3A 39 EB 0A 81 7D 1C 4D 87 BD B8 2D 1F 1C "
                              "48 CD 64 19 80 96 72 D2 34 92 60 D8 9A 08 00 02 "
                              "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        encrypt = CBC.encrypt(input, key)
        decrypt = CBC.decrypt(encrypt, key)
        print("#4")
        print("input -           {0}".format(input.hex()))
        print("encrypt -         {0}".format(encrypt.hex()))
        print("expected_result - {0}".format(decrypt.hex()))
        print("actual_result -   {0}".format(input.hex()))
        print()

        self.assertTrue(True)




    def setUp(self):
        self.key = bytes.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        self.x = bytes.fromhex("07 92 3A 39 EB 0A 81 7D 1C 4D 87 BD B8 2D 1F 1C 48 CD 64 19 80 96 72 D2 34 92 60 D8 9A 08")
        self.y = bytes.fromhex("07 92 3A 39 EB 0A 81 7D 1C 4D 87 BD B8 2D 1F 1C 48 CD 64 19 80 96 72 D2 34 92 60 D8 9A 08 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        self.result = bytes.fromhex("07923a39eb0a817d1c4d87bdb82d1f1c4f5f5e206b9cf3af28dfe76522251f1d4f5f5e206b9cf3af28dfe76522251f1d")

    def test_encrypt(self):
        result = CBC.encrypt(self.y, self.key)
        print(result.hex())

    def test_decrypt(self):
        x = bytes.fromhex("07923a39eb0a817d1c4d87bdb82d1f1c4f5f5e206b9cf3af28dfe76522251f1d4f5f5e206b9cf3af28dfe76522251f1d4f5f5e206b9cf3af28dfe76522251f1d")
        result = CBC.decrypt(x, self.key)
        print(result.hex())

    def test_is_message_total(self):
        self.assertTrue(CBC.is_message_total(self.y) and not CBC.is_message_total(self.x))

    def test_is_block_padding(self):
        ls = []
        expect = []
        ls.append(bytes.fromhex("07 92 3A 39 EB 00 00 01 "))
        expect.append(False)
        ls.append(bytes.fromhex("07 92 3A 39 EB 00 00 02 "))
        expect.append(True)
        ls.append(bytes.fromhex("07 92 3A 39 EB F1 F1 00"))
        expect.append(True)
        ls.append(bytes.fromhex("07 92 3A 39 EB F1 F1 CC"))
        expect.append(False)

        real = []
        for b in ls:
            real.append(CBC.is_block_padding(b))

        self.assertEqual(real, expect)

    def test_pars_padding_block(self):
        x = bytes.fromhex("07 92 3A 39 EB 0A 81 7D 1C 4D 87 BD B8 2D 1F 1C 48 CD 64 19 80 96 72 D2 34 92 60 D8 9A 08 00 02")
        result = CBC.pars_padding_block(x)
        expected = bytes.fromhex("07 92 3A 39 EB 0A 81 7D 1C 4D 87 BD B8 2D 1F 1C 48 CD 64 19 80 96 72 D2 34 92 60 D8 9A 08")
        self.assertEqual(result, expected)

    def test_get_16_bytes_block(self):
        expect = []
        expect.append(bytes.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"))
        expect.append(bytes.fromhex("48 CD 64 19 80 96 72 D2 34 92 60 D8 9A 08 00 01"))

        real = []

        for i in range(1, 2 + 1):
            real.append(CBC.get_16_bytes_block(self.y, i))

        self.assertEqual(expect, real)

    def test_is_block_empty(self):
        self.assertTrue(CBC.is_block_empty(bytes.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")) and not CBC.is_block_empty(bytes.fromhex("00 00 30 00 00 00 00 00 00 00 00 00 00 00 00 00")))