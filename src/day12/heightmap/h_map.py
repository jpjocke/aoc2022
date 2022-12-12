from typing import List

from src.day12.heightmap.h_map_point import HeightMapPoint


class HeightMap:
    map: List[List[HeightMapPoint]]
    start: HeightMapPoint
    end: HeightMapPoint

    def print(self):
        for y in self.map:
            sb = ""
            for x in y:
                sb += x.height
            print(sb)