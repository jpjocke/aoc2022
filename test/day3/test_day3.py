import unittest

from src.day3.rug.rugsack_parser import parse_rugsacks, value_converter
from src.util.file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day3_test_in.txt")
        rugs = parse_rugsacks(data)
        total = 0
        for rug in rugs:
            dup = rug.find_duplicates()
            total += value_converter(dup)

        self.assertEqual(157, total)

    def test_problem_2(self):
        self.assertEqual(12, 12)


if __name__ == '__main__':
    unittest.main()
