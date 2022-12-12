from typing import List

from src.day12.heightmap.h_map import HeightMap
from src.day12.heightmap.h_map_point import HeightMapPoint
from src.util.point import Point


def parse_h_map(data: List[str]) -> HeightMap:
    h_map = HeightMap()
    full = []
    for y, row in enumerate(data):
        r_list = []
        for x, letter in enumerate(row):
            p = Point(x, y)
            h_map_point = HeightMapPoint()
            h_map_point.p = p
            if letter == "S":
                h_map_point.height = "a"
                h_map_point.start_point = True
                h_map.start = h_map_point
            elif letter == "E":
                h_map_point.height = "z"
                h_map_point.end_point = True
                h_map.end = h_map_point
            else:
                h_map_point.height = letter
            h_map_point.value = ord(h_map_point.height)
            r_list.append(h_map_point)
        full.append(r_list)
    h_map.map = full
    return h_map
