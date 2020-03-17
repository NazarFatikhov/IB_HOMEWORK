from bitarray import bitarray

class ByteUtils:

    def getLeftPart(bytes):
        return bytes[:int(len(bytes) / 2)]

    def getRightPart(bytes):
        return bytes[int(len(bytes) / 2):]

    def xor(first, second):
        if (not len(first) == len(second)):
            raise ValueError("operators should have same size")
        result = bytes()
        for ind in range(len(first)):
            result += bytes([first[ind] ^ second[ind]])
        return result

    def lor(bytes, count):
        _bitarray = bitarray(endian='big')
        _bitarray.frombytes(bytes)

        buf = bitarray(endian='big')
        for i in range(count):
            buf.append(_bitarray[i])
        for i in range(len(_bitarray) - count):
            buf.insert(0, 0)

        for i in range(len(_bitarray) - count):
            _bitarray[i] = _bitarray[i + count]

        _bitarray = _bitarray ^ buf

        return _bitarray.tobytes()
