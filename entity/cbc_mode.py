from entity.cameila import Camelia
from entity.byte_utils import ByteUtils

class CBC:

    def encrypt(x: bytes, key: bytes):
        if (len(x) < 16):
            raise Exception("text should contain more or equal than 16 bytes")
        elif (len(key) != 16):
            raise Exception("text should have 16 bytes")

        if (CBC.is_message_total(x)):
            if (CBC.is_block_empty(CBC.get_16_bytes_block(x, 1))):
                if (CBC.is_block_padding(CBC.get_16_bytes_block(x, 2))):
                    text = x + int(0).to_bytes(16, "little")
                    return CBC.encrypt_if_block_total(text, key)
                else:
                    return CBC.encrypt_if_block_total(x, key)
            else:
                return CBC.encrypt_if_block_total(x, key)
        else:
            return CBC.encrypt_if_block_not_total(x, key)

    def encrypt_if_block_total(x: bytes, key: bytes):
        count = len(x) // 16
        blocks = []

        for i in range(1, count + 1):
            blocks.append(x[16 * (i - 1): 16 * i])

        cipher_blocks = []
        init_block = key
        for i in range(len(blocks)):
            cipher_block = ByteUtils.xor(blocks[i], init_block)
            cipher_blocks.append(cipher_block)
            init_block = cipher_block

        result = bytes()
        for block in cipher_blocks:
            result += block

        return result

    def encrypt_if_block_not_total(x: bytes, key: bytes):
        count = len(x) // 16
        blocks = []

        for i in range(1, count + 1):
            blocks.append(x[16 * (i - 1): 16 * i])

        last_bloc = x[16 * count: len(x)]

        if(len(last_bloc) == 16):
            blocks.append(last_bloc)
        else:
            empty_bytes = 0
            while(len(last_bloc) < 15):
                empty_bytes += 1
                last_bloc += int(0).to_bytes(1, "little")
            last_bloc += int(empty_bytes).to_bytes(1, "little")
            blocks.append(last_bloc)
            blocks.append(int(0).to_bytes(16, "little"))

        cipher_blocks = []
        init_block = key
        for i in range(len(blocks)):
            cipher_block = ByteUtils.xor(blocks[i], init_block)
            cipher_blocks.append(cipher_block)
            init_block = cipher_block

        result = bytes()
        for block in cipher_blocks:
            result += block

        return result

    def decrypt(x: bytes, key: bytes):
        if (len(x) < 16):
            raise Exception("text should contain more or equal than 16 bytes")
        elif (len(key) != 16):
            raise Exception("text should have 16 bytes")
        elif (len(x) % 16 != 0):
            raise Exception("text should have total each block")

        count = len(x) // 16
        blocks = []

        for i in range(1, count + 1):
            blocks.append(x[16 * (i - 1): 16 * i])

        cipher_blocks = []
        init_block = key
        for i in range(len(blocks)):
            cipher_block = ByteUtils.xor(blocks[i], init_block)
            cipher_blocks.append(cipher_block)
            init_block = blocks[i]

        result = bytes()
        for block in cipher_blocks:
            result += block

        if (CBC.is_block_empty(CBC.get_16_bytes_block(result, 1))):
            return CBC.handle_decrypt_if_last_block_empty(result)
        else:
            return result

    def handle_decrypt_if_last_block_empty(x: bytes):
        if (CBC.is_block_empty(CBC.get_16_bytes_block(x, 2))):
            if(CBC.is_block_padding(CBC.get_16_bytes_block(x, 3))):
                return x[:len(x) - 16]
            else:
                return x
        else:
            if(CBC.is_block_padding(CBC.get_16_bytes_block(x, 2))):
                return CBC.pars_padding_block(x[:len(x) - 16])
            else:
                return x

    def handle_decrypt_if_3_block_padding(x: bytes):
        if(CBC.is_block_padding(CBC.get_16_bytes_block(x, 3))):
            return x[len(x) - 16]
        else:
            return x


    def is_message_total(x: bytes):
        return len(x) % 16 == 0

    def is_block_padding(x: bytes):
        count = x[-1]
        k = 0
        i = -2
        while x[i] == 0 and abs(i) < len(x):
            k += 1
            i -= 1
        if k == count:
            return True
        return False

    def pars_padding_block(x: bytes):
        if (len(x) % 16 != 0):
            raise Exception("block should have total blocks")
        count = int(x[-1])
        return x[: len(x) - 1 - count]

    def get_16_bytes_block(x: bytes, n: int):
        if (len(x) < n * 16):
            raise Exception("sequence should have not less than {0} bytes".format(n * 16))
        if (n < 1):
            raise Exception("count should be more than {0}".format(0))
        return x[16 * (len(x)//16 - n):16 * (len(x)//16 - n) + 16]

    def is_block_empty(x: bytes):
        if(len(x) != 16):
            raise Exception("block should have  bytes")
        return x == bytes.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")