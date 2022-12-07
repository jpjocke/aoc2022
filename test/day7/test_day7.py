import unittest

from src.day7.file_system.file_system_traverser import find_total_size_for_problem_1
from src.day7.file_system.file_system_parser import FileSystemParser
from src.util.file_reader import FileReader


class TestDaySeven(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day7_test_in.txt")
        fs_parser = FileSystemParser()
        root = fs_parser.parse_file_system(data)
        root.print()
        total_size = find_total_size_for_problem_1(root=root)
        self.assertEqual(95437, total_size)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day7_test_in.txt")
        self.assertEqual(19, 19)


if __name__ == '__main__':
    unittest.main()
