from entity.byte_utils import ByteUtils

class Key:
    S_1 = bytes.fromhex("a0 9e 66 7f 3b cc 90 8b")
    S_2 = bytes.fromhex("b6 7a e8 58 4c aa 73 b2")
    S_3 = bytes.fromhex("c6 ef 37 2f e9 4f 82 be")
    S_4 = bytes.fromhex("54 ff 53 a5 f1 d3 6f 1c")


    def __init__(self, key) -> None:
        self.key = key

    def q_key(self):

        #part 1
        left_part = ByteUtils.getLeftPart(self.key)
        left_part_xor_s1 = ByteUtils.xor(left_part, self.S_1)
        right_part = ByteUtils.xor(left_part_xor_s1, ByteUtils.getRightPart(self.key))

        #part 2
        left_part, right_part = right_part, left_part
        left_part_xor_s2 = ByteUtils.xor(left_part, self.S_2)
        right_part = ByteUtils.xor(left_part_xor_s2, right_part)

        #part 3
        left_part, right_part = right_part, left_part
        part_3_res = left_part + right_part

        #part 4
        part_4_res = ByteUtils.xor(part_3_res, self.key)

        #part 5
        left_part = ByteUtils.getLeftPart(part_4_res)
        right_part = ByteUtils.getRightPart(part_4_res)
        left_part_xor_s3 = ByteUtils.xor(right_part, self.S_3)

        #part 6
        left_part, right_part = right_part, left_part
        left_part_xor_s4 = ByteUtils.xor(left_part, self.S_4)
        right_part = ByteUtils.xor(right_part, left_part_xor_s4)

        return right_part + left_part

