import unittest

from src.day12.heightmap.diff_start import find_shortest_for_different_start_pos
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
        h_map = parse_h_map(data)
        shortest = find_shortest_for_different_start_pos(h_map)
        self.assertEqual(29, shortest)


if __name__ == '__main__':
    unittest.main()
