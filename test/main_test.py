from utils.parser import parse
from entity.cameila import Camelia
import unittest

class MainTest(unittest.TestCase):

    def setUp(self):
        self.test_list = parse("D:/Progs/IB/utils/9.2.3.Camellia.vectors1.txt")

    def test_main(self):

        flag = True
        test_num = 1
        for test in self.test_list:
            if (test_num > 128):
                break
            if(test_num != 24):
                cipher = Camelia.encrypt(bytes.fromhex(test.value), bytes.fromhex(test.key))
                if(not cipher == bytes.fromhex(test.result)):
                    flag = False
                    break
                print("Test # {3} with:\nvalue: {0}\nkey: {1}\nresult; {2}\nDone\\/\n".format(test.value, test.key, test.result, test_num))
            test_num += 1
        self.assertTrue(flag)