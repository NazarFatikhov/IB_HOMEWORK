from entity.cameila import Camelia
from entity.byte_utils import ByteUtils

class CBC:

    def encrypt(x: bytes, key: bytes):
        if(len(x) < 16):
            raise Exception("text should contain more or equal than 16 bytes")
        elif(len(key) != 16):
            raise Exception("text should have 16 bytes")

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
            cipher_block = Camelia.encrypt(ByteUtils.xor(blocks[i], init_block), key)
            cipher_blocks.append(cipher_block)
            init_block = cipher_block

        result = bytes()
        for block in cipher_blocks:
            result += block

        return result