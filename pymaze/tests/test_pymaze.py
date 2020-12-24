from unittest import TestCase
import pymaze.pymaze


class Test(TestCase):
    def test_pyMaze_makemaze(self):
        tmp = pymaze.pymaze.pyMaze_makemaze(7, 9)
        pymaze.pymaze.pyMaze_draw(tmp)

