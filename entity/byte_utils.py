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

    def rol(bytes, count):
        _bitarray = bitarray(endian='big')
        _bitarray.frombytes(bytes)

        buf = _bitarray[0:count]
        for i in range(len(_bitarray) - count):
            _bitarray[i] = _bitarray[i + count]

        for i in range(len(buf)):
            _bitarray[len(_bitarray) - count + i] = buf[i]

        return _bitarray.tobytes()

    def ror(bytes, count):
        _bitarray = bitarray(endian='big')
        _bitarray.frombytes(bytes)

        buf = bitarray(endian='big')
        for i in range(len(_bitarray) - count, len(_bitarray)):
            buf.append(_bitarray[i])
        for i in range(0, len(_bitarray) - count):
            buf.append(_bitarray[i])

        return buf.tobytes()
