import unittest

from src.day8.forest.forest import Forest
from src.util.file_reader import FileReader


class TestDayEight(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day8_test_in.txt")
        forest = Forest(data=data)
        print(forest.forest)
        visible = forest.find_visible()
        print(forest.visible)
        self.assertEqual(21, visible)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day8_test_in.txt")
        self.assertEqual(24933642, 24933642)


if __name__ == '__main__':
    unittest.main()
