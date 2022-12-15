from typing import List

from src.day15.sensor.sensor import Sensor
from src.util.point import Point


def parse_sensors(data: List[str]) -> List[Sensor]:
    sensors = []
    for row in data:
        # print(row)
        row = row.replace(":", "").replace(",", "")
        split = row.split(" ")
        s_x = _split_loc(split[2])
        s_y = _split_loc(split[3])
        sensor_point = Point(x=s_x, y=s_y)
        b_x = _split_loc(split[8])
        b_y = _split_loc(split[9])
        beacon_point = Point(x=b_x, y=b_y)
        s = Sensor()
        s.pos = sensor_point
        s.beacon = beacon_point
        s.calculate_man_reach()
        sensors.append(s)
    return sensors


def _split_loc(loc: str) -> int:
    split = loc.split("=")
    return int(split[1])
