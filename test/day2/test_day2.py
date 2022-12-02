import unittest

from src.day2.rps.rps_constructor import parse_rps, count_score
from src.util.file_reader import FileReader


class TestDayOne(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day2_test_in.txt")
        rpss = parse_rps(data)
        score = count_score(rpss)

        self.assertEqual(15, score)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day2_test_in.txt")
        self.assertEqual(45000, 45000)


if __name__ == '__main__':
    unittest.main()
