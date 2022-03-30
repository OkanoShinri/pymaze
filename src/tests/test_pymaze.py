from unittest import TestCase
import pymaze.pymaze


class Test(TestCase):
    def test_makemaze(self):
        tmp = pymaze.pymaze.makemaze(31, 31)
        self.assertEqual(type(tmp), list)
        self.assertEqual(type(tmp[0]), list)
        self.assertEqual(tmp[2][2], 2)
        self.assertEqual(tmp[31 - 1][31 - 1], 2)


"""
class Test(TestCase):
    def test_pymaze(self):
        pymaze.pymaze.pymaze()
"""
