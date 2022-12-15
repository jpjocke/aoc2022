from typing import List

from src.day15.sensor.sensor import Sensor
from src.util.point import Point


def check_coverage(sensors: List[Sensor], row: int) -> int:
    points = set()
    for s in sensors:
        line = s.get_coverage_on_row(row)
        for p in line:
            points.add(p)

    for s in sensors:
        if s.beacon in points:
            points.remove(s.beacon)
    return len(points)


class BeaconFinder:
    x: int
    y: int
    max: int
    sensors: List[Sensor]

    def __init__(self, sensors: List[Sensor], max_size: int):
        self.x = 0
        self.y = 0
        self.max = max_size
        self.sensors = sensors

    def find(self) -> int:
        while True:
            if self.x > self.max:
                self.x = 0
                self.y += 1
            pos = Point(x=self.x, y=self.y)
            if self._test_pos(pos=pos):
                return self.x * 4000000 + self.y

    def _test_pos(self, pos: Point) -> bool:
        for s in self.sensors:
            man_dist = s.pos.distance(pos)
            if man_dist <= s.man_reach:
                dist_x = abs(self.y - s.pos.y)
                self.x = s.pos.x + (s.man_reach - dist_x) + 1
                return False
        return True
