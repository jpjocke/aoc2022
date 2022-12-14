from typing import List

from src.util.point import Point


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_line(self) -> List[Point]:
        line = []
        x = self.start.x
        y = self.start.y
        while True:
            line.append(Point(x, y))
            if x == self.end.x and y == self.end.y:
                break
            x = self.__next_val(x, self.end.x)
            y = self.__next_val(y, self.end.y)
        return line

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def __next_val(self, val: int, max: int) -> int:
        if val == max:
            return val
        elif val < max:
            return val + 1
        return val - 1

    def __str__(self):
        return 'S: {' + self.start.__str__() + '}, E: {' + self.end.__str__() + '}'
