from src.day12.heightmap.h_map_solver import HeightMapSolver
from src.day12.heightmap.h_map import HeightMap


def find_shortest_for_different_start_pos(h_map: HeightMap) -> int:
    shortest = 999999
    for y, row in enumerate(h_map.map):
        for x, h_p in enumerate(row):
            if h_p.height == "a":
                h_map.start = h_p
                solver = HeightMapSolver(h_map)
                s = solver.solve_shortest()
                if s < shortest:
                    shortest = s
    return shortest
