from typing import List

from src.util.point import Point


class Sensor:
    pos: Point
    beacon: Point
    man_reach: int

    def calculate_man_reach(self):
        self.man_reach = self.pos.distance(self.beacon)

    def get_coverage_on_row(self, row: int) -> List[Point]:
        x = self.pos.x
        points = []
        while True:
            test = Point(x=x, y=row)
            if test.distance(self.pos) > self.man_reach:
                break
            points.append(test)
            if x != self.pos.x:
                other_side = self.pos.x - (x - self.pos.x)
                points.append(Point(x=other_side, y=row))
            x += 1

        return points
