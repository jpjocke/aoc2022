import unittest

from src.day1.cal.calories_builder import build_c, find_highest, find_top_three_sum
from src.util.file_reader import FileReader


class TestDayOne(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day1_test_in.txt")
        cs = build_c(data)
        max_c = find_highest(cs)

        self.assertEqual(24000, max_c.sum())

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day1_test_in.txt")
        cs = build_c(data)
        sum_3 = find_top_three_sum(cs)
        self.assertEqual(45000, sum_3)


if __name__ == '__main__':
    unittest.main()
