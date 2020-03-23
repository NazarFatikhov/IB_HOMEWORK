from entity.byte_utils import ByteUtils
from entity.f_function import FFunc

class Key:
    S_1 = bytes.fromhex("a0 9e 66 7f 3b cc 90 8b")
    S_2 = bytes.fromhex("b6 7a e8 58 4c aa 73 b2")
    S_3 = bytes.fromhex("c6 ef 37 2f e9 4f 82 be")
    S_4 = bytes.fromhex("54 ff 53 a5 f1 d3 6f 1c")

    def q_key(k: bytes):

        #part 1
        left_part = ByteUtils.getLeftPart(k)
        sqr_1 = FFunc.f_func(left_part, Key.S_1)
        right_part = ByteUtils.xor(sqr_1, ByteUtils.getRightPart(k))

        #part 2
        left_part, right_part = right_part, left_part
        sqr_2 = FFunc.f_func(left_part, Key.S_2)
        right_part = ByteUtils.xor(sqr_2, right_part)

        #part 3
        left_part, right_part = right_part, left_part
        part_3_res = ByteUtils.xor(left_part + right_part, k)

        #part 4
        left_part = ByteUtils.getLeftPart(part_3_res)
        right_part = ByteUtils.getRightPart(part_3_res)
        sqr_3 = FFunc.f_func(left_part, Key.S_3)
        right_part = ByteUtils.xor(sqr_3, right_part)

        #part 5
        left_part, right_part = right_part, left_part
        sqr_4 = FFunc.f_func(left_part, Key.S_4)
        right_part = ByteUtils.xor(sqr_4, right_part)

        return right_part + left_part

