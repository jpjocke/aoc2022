import unittest

from src.day5.stacks.stack_parser import parse_stacks
from src.util.file_reader import FileReader


class TestDayFive(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day5_test_in.txt")
        stacks = parse_stacks(data)
        stacks.print()
        stacks.run_instructions()
        stacks.print()
        self.assertEqual("CMZ", stacks.get_code())

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day5_test_in.txt")
        self.assertEqual(4, 4)


if __name__ == '__main__':
    unittest.main()
