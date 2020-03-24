from entity.key import Key
from entity.byte_utils import ByteUtils
from entity.f_function import FFunc
from entity.fl_function import FLFunction

class Camelia:

    k_i = []
    kw_i = []
    kl_i = []

    def init_key_k(key: bytes):
        key_q = Key.q_key(key)

        Camelia.k_i = [
            ByteUtils.getLeftPart(key_q), ByteUtils.getRightPart(key_q),
            ByteUtils.getLeftPart(ByteUtils.rol(key, 15)), ByteUtils.getRightPart(ByteUtils.rol(key, 15)),
            ByteUtils.getLeftPart(ByteUtils.rol(key_q, 15)), ByteUtils.getRightPart(ByteUtils.rol(key_q, 15)),
            ByteUtils.getLeftPart(ByteUtils.rol(key, 45)), ByteUtils.getRightPart(ByteUtils.rol(key, 45)),
            ByteUtils.getLeftPart(ByteUtils.rol(key_q, 45)), ByteUtils.getRightPart(ByteUtils.rol(key, 60)),
            ByteUtils.getLeftPart(ByteUtils.rol(key_q, 60)), ByteUtils.getRightPart(ByteUtils.rol(key_q, 60)),
            ByteUtils.getLeftPart(ByteUtils.rol(key, 94)), ByteUtils.getRightPart(ByteUtils.rol(key, 94)),
            ByteUtils.getLeftPart(ByteUtils.rol(key_q, 94)), ByteUtils.getRightPart(ByteUtils.rol(key_q, 94)),
            ByteUtils.getLeftPart(ByteUtils.rol(key, 111)), ByteUtils.getRightPart(ByteUtils.rol(key, 111)),
        ]

        Camelia.kl_i = [
            ByteUtils.getLeftPart(ByteUtils.rol(key_q, 30)), ByteUtils.getRightPart(ByteUtils.rol(key_q, 30)),
            ByteUtils.getLeftPart(ByteUtils.rol(key, 77)), ByteUtils.getRightPart(ByteUtils.rol(key, 77)),
        ]

        Camelia.kw_i = [
            ByteUtils.getLeftPart(key), ByteUtils.getRightPart(key),
            ByteUtils.getLeftPart(ByteUtils.rol(key_q, 111)), ByteUtils.getRightPart(ByteUtils.rol(key_q, 111))
        ]

    def encrypt(x: bytes, key: bytes):
        if(len(x) != 16):
            raise Exception("entry value should be 16 bytes")
        elif(len(key) != 16):
            raise Exception("key should be 16 bytes")

        Camelia.init_key_k(key)

        left = ByteUtils.xor(ByteUtils.getLeftPart(x), Camelia.kw_i[0])
        right = ByteUtils.xor(ByteUtils.getRightPart(x), Camelia.kw_i[1])

        for i in range(6):
            sqr = FFunc.f_func(left, Camelia.k_i[i])
            right = ByteUtils.xor(right, sqr)
            right, left = left, right

        left = FLFunction.fl_func(left, Camelia.kl_i[0])
        right = FLFunction.fl_inv(right, Camelia.kl_i[1])

        for i in range(6, 12):
            sqr = FFunc.f_func(left, Camelia.k_i[i])
            right = ByteUtils.xor(right, sqr)
            right, left = left, right

        left = FLFunction.fl_func(left, Camelia.kl_i[2])
        right = FLFunction.fl_inv(right, Camelia.kl_i[3])

        for i in range(12, 18):
            sqr = FFunc.f_func(left, Camelia.k_i[i])
            right = ByteUtils.xor(right, sqr)
            right, left = left, right

        left, right = ByteUtils.xor(right, Camelia.kw_i[2]),ByteUtils.xor(left, Camelia.kw_i[3])

        return left + right
