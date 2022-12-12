import time

from src.day12.heightmap.diff_start import find_shortest_for_different_start_pos
from src.day12.heightmap.h_map_parser import parse_h_map
from src.day12.heightmap.h_map_solver import HeightMapSolver
from src.util.file_reader import FileReader

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day12_in.txt")
h_map = parse_h_map(data)
solver = HeightMapSolver(h_map)
shortest = solver.solve_shortest()
print(f"problem1: {shortest}")

shortest_2 = find_shortest_for_different_start_pos(h_map)
print(f"problem2: {shortest_2}")

print("--- %s seconds ---" % (time.time() - start_time))
