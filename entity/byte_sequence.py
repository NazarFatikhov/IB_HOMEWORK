from bitarray import bitarray

class ByteSequence:

    def __init__(self, right, left):
        self.leftBytes = right
        self.rightBytes = left

    @classmethod
    def from_bytes_string(self, bytes_string):
        self.leftBytes = bytes_string[:int(len(bytes_string) / 2)]
        self.rightBytes = bytes_string[int(len(bytes_string) / 2):]
        return self

    def full_bytes(self):
        return self.leftBytes + self.rightBytes

    def __eq__(self, other):
        return self.full_bytes().__eq__(other.full_bytes())

    def xor(self, other):
        if (not len(other) == len(self.full_bytes(self))):
            raise ValueError("operators should have same size")
        result = bytes()
        for ind in range(len(self.full_bytes(self))):
            result += bytes([self.full_bytes(self)[ind] ^ other[ind]])
        return ByteSequence.from_bytes_string(result)

    def lor(self, count):
        _bitarray = bitarray(endian='big')
        _bitarray.frombytes(self.full_bytes(self))

        buf = bitarray(endian='big')
        for i in range(count):
            buf.append(_bitarray[i])
        for i in range(len(_bitarray) - count):
            buf.insert(0, 0)

        for i in range(len(_bitarray) - count):
            _bitarray[i] = _bitarray[i + count]

        _bitarray = _bitarray ^ buf

        return ByteSequence.from_bytes_string(_bitarray.tobytes())
