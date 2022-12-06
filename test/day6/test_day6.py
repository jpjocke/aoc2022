import unittest

from src.day6.buffer.signal_finder import find_start_of_packet, find_start_of_message
from src.util.file_reader import FileReader


class TestDaySix(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day6_test_in.txt")
        start = find_start_of_packet(data[0])
        self.assertEqual(7, start)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day6_test_in.txt")
        start = find_start_of_message(data[0], 0)
        self.assertEqual(19, start)


if __name__ == '__main__':
    unittest.main()
