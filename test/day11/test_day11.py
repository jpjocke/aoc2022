import unittest

from src.day11.monkey.monkey_runner import run_monkeys
from src.day11.monkey.monkey_parser import parse_monkeys
from src.util.file_reader import FileReader


class TestDayEleven(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day11_test_in.txt")
        monkeys = parse_monkeys(data)
        monkey_business = run_monkeys(monkeys, 20)
        self.assertEqual(10605, monkey_business)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day11_test_in.txt")
        self.assertEqual(36, 36)


if __name__ == '__main__':
    unittest.main()
