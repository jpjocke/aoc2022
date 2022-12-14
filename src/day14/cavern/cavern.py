from typing import List

from src.day14.cavern.cavern_point import CavernPoint
from src.util.point import Point


class Cavern:
    c_map: List[List[CavernPoint]]

    def __init__(self):
        self.c_map = []
        for i in range(1000):
            y = []
            self.c_map.append(y)
            for x in range(1000):
                y.append(CavernPoint())

    def add_rock(self, x: int, y: int):
        self.c_map[y][x].rock = True

    def fill_sand(self, from_p: Point) -> int:
        sand_on_edge = False
        count = 0
        while not sand_on_edge:
            sand = Point(x=from_p.x, y=from_p.y)
            sand_on_edge = self._drop_sand(sand)
            # print("-----")
            # self.print()
            count += 1
        return count - 1

    def _drop_sand(self, sand: Point) -> bool:
        while True:
            if sand.y == len(self.c_map) - 1:
                # end of map
                return True
            if not self.c_map[sand.y + 1][sand.x].is_occupied():
                # move down
                sand.y += 1
                continue
            if not self.c_map[sand.y + 1][sand.x - 1].is_occupied():
                # move down left
                sand.y += 1
                sand.x -= 1
                continue
            if not self.c_map[sand.y + 1][sand.x + 1].is_occupied():
                # move down right
                sand.y += 1
                sand.x += 1
                continue
            # nowhere to go
            self.c_map[sand.y][sand.x].sand = True
            break
        return False

    def print(self):
        for y in range(10):
            sb = ""
            for x in range(490, 510):
                sb += self.c_map[y][x].__str__()
            print(sb)
