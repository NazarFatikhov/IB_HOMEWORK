from bitarray import bitarray
from entity.byte_utils import ByteUtils


# class for calculate F function
class FFunc:
    """
        s1 table: needed to calculate S(X) function
        s1(0) = 0x70707000
        .
        .
        .
        s1(255) = 0x9e9e9e00

        as well as s1: s2, s3, s4 values
    """
    s1_arr = [
        112, 130, 44, 236, 179, 39, 192, 229, 228, 133, 87, 53, 234, 12, 174, 65,
        35, 239, 107, 147, 69, 25, 165, 33, 237, 14, 79, 78, 29, 101, 146, 189,
        134, 184, 175, 143, 124, 235, 31, 206, 62, 48, 220, 95, 94, 197, 11, 26,
        166, 225, 57, 202, 213, 71, 93, 61, 217, 1, 90, 214, 81, 86, 108, 77,
        139, 13, 154, 102, 251, 204, 176, 45, 116, 18, 43, 32, 240, 177, 132, 153,
        223, 76, 203, 194, 52, 126, 118, 5, 109, 183, 169, 49, 209, 23, 4, 215,
        20, 88, 58, 97, 222, 27, 17, 28, 50, 15, 156, 22, 83, 24, 242, 34,
        254, 68, 207, 178, 195, 181, 122, 145, 36, 8, 232, 168, 96, 252, 105, 80,
        170, 208, 160, 125, 161, 137, 98, 151, 84, 91, 30, 149, 224, 255, 100, 210,
        16, 196, 0, 72, 163, 247, 117, 219, 138, 3, 230, 218, 9, 63, 221, 148,
        135, 92, 131, 2, 205, 74, 144, 51, 115, 103, 246, 243, 157, 127, 191, 226,
        82, 155, 216, 38, 200, 55, 198, 59, 129, 150, 111, 75, 19, 190, 99, 46,
        233, 121, 167, 140, 159, 110, 188, 142, 41, 245, 249, 182, 47, 253, 180, 89,
        120, 152, 6, 106, 231, 70, 113, 186, 212, 37, 171, 66, 136, 162, 141, 250,
        114, 7, 185, 85, 248, 238, 172, 10, 54, 73, 42, 104, 60, 56, 241, 164,
        64, 40, 211, 123, 187, 201, 67, 193, 21, 227, 173, 244, 119, 199, 128, 158
    ]

    def s1(x: bytes):
        return FFunc.s1_arr[int.from_bytes(x, "little")].to_bytes(1, "little")

    def s2(x: bytes):
        s1_bytes = FFunc.s1_arr[int.from_bytes(x, "little")].to_bytes(1, "little")
        return ByteUtils.rol(s1_bytes, 1)

    def s3(x: bytes):
        s1_bytes = FFunc.s1_arr[int.from_bytes(x, "little")].to_bytes(1, "little")
        return ByteUtils.ror(s1_bytes, 1)

    def s4(x: bytes):
        rol_x = ByteUtils.rol(x, 1)
        s1_bytes = FFunc.s1_arr[int.from_bytes(rol_x, "little")].to_bytes(1, "little")
        return s1_bytes

    # S function: S(X)
    def s_func(x: bytes):
        if(len(x) != 8):
            raise Exception("operator x should have 8 bytes")

        s_bytes_arr = [
            FFunc.s1(x[0].to_bytes(1, "little")),
            FFunc.s2(x[1].to_bytes(1, "little")),
            FFunc.s3(x[2].to_bytes(1, "little")),
            FFunc.s4(x[3].to_bytes(1, "little")),
            FFunc.s2(x[4].to_bytes(1, "little")),
            FFunc.s3(x[5].to_bytes(1, "little")),
            FFunc.s4(x[6].to_bytes(1, "little")),
            FFunc.s1(x[7].to_bytes(1, "little"))
        ]

        s_bytes = bytes()

        for byte in s_bytes_arr:
            s_bytes += byte

        return s_bytes

    def p_func(x: bytes):
        if (len(x) != 8):
            raise Exception("operator x should have 8 bytes")

        p_bytes_arr = [
            x[0] ^ x[2] ^ x[3] ^ x[5] ^ x[6] ^ x[7],
            x[1] ^ x[3] ^ x[0] ^ x[6] ^ x[7] ^ x[4],
            x[2] ^ x[0] ^ x[1] ^ x[7] ^ x[4] ^ x[5],
            x[3] ^ x[1] ^ x[2] ^ x[4] ^ x[5] ^ x[6],
            x[0] ^ x[1] ^ x[5] ^ x[6] ^ x[7],
            x[1] ^ x[2] ^ x[6] ^ x[7] ^ x[4],
            x[2] ^ x[3] ^ x[7] ^ x[4] ^ x[5],
            x[3] ^ x[0] ^ x[4] ^ x[5] ^ x[6]
        ]

        p_bytes = bytes()

        for byte in p_bytes_arr:
            p_bytes += byte.to_bytes(1, "little")

        return p_bytes

    # resulting F function: F(X, k) = P(S(X xor k)))
    def f_func(x: bytes, k: bytes):
        x_xor_k_bytes = (int.from_bytes(x, "little") ^ int.from_bytes(k, "little")).to_bytes(8, "little")
        return FFunc.p_func(FFunc.s_func(x_xor_k_bytes))