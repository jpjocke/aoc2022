import time

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

print(f"problem2: {2}")

print("--- %s seconds ---" % (time.time() - start_time))
