from typing import List

from src.day1.cal.calories import Calories


def build_c(raw: List[str]) -> List[Calories]:
    cs = []
    c = Calories()
    cs.append(c)
    for row in raw:
        if len(row) == 0:
            c = Calories()
            cs.append(c)
        else:
            c.add_c(int(row))
    return cs


def find_highest(cs: List[Calories]) -> Calories:
    max = 0
    ret = None
    for c in cs:
        if c.sum() > max:
            ret = c
            max = c.sum()
    return ret


def find_top_three_sum(cs: List[Calories]) -> int:
    tot_list = [c.sum() for c in cs]
    tot_list.sort()
    tot_list = tot_list[-3:]
    for t in tot_list:
        print(t)
    return sum(tot_list)
