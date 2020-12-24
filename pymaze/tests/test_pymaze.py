from unittest import TestCase
import pymaze.pymaze


class Test(TestCase):
    def test_pyMaze_makemaze(self):
        tmp = pymaze.pymaze.pyMaze_makemaze(7, 9)
        self.assertEqual(type(tmp), list)
        self.assertEqual(0, tmp[2][2])

