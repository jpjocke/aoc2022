from typing import List

from src.day15.sensor.sensor import Sensor


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
