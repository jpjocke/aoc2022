import unittest

from src.day9.rope.rope import Rope
from src.util.file_reader import FileReader


class TestDayNine(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day9_test_in.txt")
        rope = Rope(2)
        rope.run(data)
        visited = rope.count_visited()
        self.assertEqual(13, visited)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day9b_test_in.txt")
        rope = Rope(10)
        rope.run(data)
        visited = rope.count_visited()
        self.assertEqual(visited, 36)


if __name__ == '__main__':
    unittest.main()
