import unittest

from src.day4.section.sections_parser import parse_sections, count_fits
from src.util.file_reader import FileReader


class TestDayFour(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day4_test_in.txt")
        sections_list = parse_sections(data)
        count = count_fits(sections_list)

        self.assertEqual(2, count)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day4_test_in.txt")
        self.assertEqual(70, 70)


if __name__ == '__main__':
    unittest.main()
