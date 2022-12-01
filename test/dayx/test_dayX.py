import unittest

from src.util.file_reader import FileReader


class TestDayOne(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_int_lines("../data/dayX_in.txt")

        self.assertEqual(137, data[0])

    def test_problem_2(self):
        self.assertEqual(5, 5)


if __name__ == '__main__':
    unittest.main()
