import unittest

from src.day12.heightmap.h_map_solver import HeightMapSolver
from src.day12.heightmap.h_map_parser import parse_h_map
from src.util.file_reader import FileReader


class TestDayTwelve(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day12_test_in.txt")
        h_map = parse_h_map(data)
        solver = HeightMapSolver(h_map)
        shortest = solver.solve_shortest()
        self.assertEqual(31, shortest)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day12_test_in.txt")
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
