import unittest

from src.day8.forest.forest import Forest
from src.util.file_reader import FileReader


class TestDayEight(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day8_test_in.txt")
        forest = Forest(data=data)
        visible = forest.find_visible()
        self.assertEqual(21, visible)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day8_test_in.txt")
        forest = Forest(data=data)
        scenic = forest.find_scenic()
        self.assertEqual(8, scenic)


if __name__ == '__main__':
    unittest.main()
