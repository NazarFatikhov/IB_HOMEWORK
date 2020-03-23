from entity.byte_utils import ByteUtils

class FLFunction:

    def fl_func(x: bytes, kl: bytes):
        x_l = ByteUtils.getLeftPart(x)
        x_r = ByteUtils.getRightPart(x)
        kl_l = ByteUtils.getLeftPart(kl)
        kl_r = ByteUtils.getRightPart(kl)

        sqr_1 = int(int.from_bytes(kl_l, "little") & int.from_bytes(x_l, "little")).to_bytes(4, "little")
        sqr_2 = ByteUtils.rol(sqr_1, 1)
        sqr_3 = ByteUtils.xor(sqr_2, x_r)
        sqr_4 = (int.from_bytes(sqr_3, "little") | int.from_bytes(kl_r, "little")).to_bytes(4, "little")
        sqr_5 = ByteUtils.xor(sqr_4, x_l)

        return sqr_5 + sqr_3

    def fl_inv(y: bytes, kl: bytes):
        y_l = ByteUtils.getLeftPart(y)
        y_r = ByteUtils.getRightPart(y)
        kl_l = ByteUtils.getLeftPart(kl)
        kl_R = ByteUtils.getRightPart(kl)

        sqr_1 = (int.from_bytes(y_r, "little") | int.from_bytes(kl_R, "little")).to_bytes(4, "little")
        sqr_2 = ByteUtils.xor(sqr_1, y_l)
        sqr_3 = (int.from_bytes(sqr_2, "little") & int.from_bytes(kl_l, "little")).to_bytes(4, "little")
        sqr_4 = ByteUtils.rol(sqr_3, 1)
        sqr_5 = ByteUtils.xor(sqr_4, y_r)

        return sqr_2 + sqr_5