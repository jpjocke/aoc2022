import unittest

from src.day14.cavern.cavern_parser import parse_cavern
from src.util.file_reader import FileReader
from src.util.point import Point


class TestDayFourteen(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day14_test_in.txt")
        cavern = parse_cavern(data)
        cavern.print()
        count = cavern.fill_sand(from_p=Point(x=500, y=0))
        self.assertEqual(24, count)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day14_test_in.txt")
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
