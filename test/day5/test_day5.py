import unittest

from src.day5.stacks.stack_parser import parse_stacks
from src.util.file_reader import FileReader


class TestDayFive(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day5_test_in.txt")
        stacks = parse_stacks(data)
        stacks.run_instructions()
        self.assertEqual("CMZ", stacks.get_code())

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day5_test_in.txt")
        stacks = parse_stacks(data)
        stacks.run_instructions_2()
        self.assertEqual("MCD", stacks.get_code())


if __name__ == '__main__':
    unittest.main()
