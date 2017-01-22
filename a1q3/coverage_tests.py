import unittest
from a1q3 import M

class CoverageTests (unittest.TestCase):
    def test_1 (self):
        """run all cases via node 8 to finish node coverage
        TRNC = {3, 8, 9, 12, 13, 14, 17, 18, 21, 23, 24, 26, 27}"""
        o = M()
        arg_list = [['', 0], ['e', 0], ['es', 0], ['esh', 0]]
        for arg in arg_list:
            o.m(arg[0], arg[1])
    def test_2 (self):
        """let one case not go via node 8 to cover the path (3,9)
        TREC = {[3,8], [3,9], [8,9], [9,12], [9,13], [12,23], [13,14], [13,17],
        [14,23], [17,18], [17,21], [18,23], [21,23], [23,24], [23,26], [24,27], [26,27]}
        """
        o = M()
        arg_list = [['', 1], ['e', 0], ['es', 0], ['esh', 0]]
        for arg in arg_list:
            o.m(arg[0], arg[1])
    def test_3 (self):
        """let one case go via both node 8 and node 12 to achieve EPC coverage
        TREPC = {[3,8,9], [3,9,12], [3,9,13], [8,9,12], [8,9,13], [9,12,23], [9,13,14], [9,13,17],
        , [12,23,26], [13,14,23], [13,17,18], [13,17,21], [14,23,24], [17,18,23],
        [17,21,23], [18,23,24], [21,23,24], [23,24,27], [23,26,27]}
        """
        o = M()
        arg_list = [['', 1], ['', 0], ['e', 0], ['es', 0], ['esh', 0]]
        for arg in arg_list:
            o.m(arg[0], arg[1])
    def test_4 (self):
        """let the test cases cover all situations
        TRPPC = {[3,8,9,12,23,26,27], [3,8,9,13,14,23,26,27], [3,8,9,13,17,18,23,26,27], [3,8,9,13,17,21,23,26,27],
         [3,9,12,23,26,27], [3,9,13,14,23,24,27], [3,9,13,17,18,23,24,27], [3,9,13,17,21,23,24,27]}
        """
        o = M()
        arg_list = [['', 0], ['e', 0], ['es', 0], ['esh', 0], ['', 1], ['e', 1], ['es', 1], ['esh', 1]]
        for arg in arg_list:
            o.m(arg[0], arg[1])
    
