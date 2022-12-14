from typing import List

from src.day14.cavern.cavern import Cavern
from src.util.point import Point
from src.util.line import Line


def parse_cavern(data: List[str]) -> Cavern:
    cavern = Cavern()
    for row in data:
        row = row.replace(" ", "")
        split = row.split("->")
        for i in range(len(split) - 1):
            inner_s_1 = split[i].split(",")
            s_point = Point(x=int(inner_s_1[0]), y=int(inner_s_1[1]))
            inner_s_2 = split[i+1].split(",")
            e_point = Point(x=int(inner_s_2[0]), y=int(inner_s_2[1]))
            line = Line(start=s_point, end=e_point)
            for p in line.get_line():
                cavern.add_rock(x=p.x, y=p.y)
    return cavern
