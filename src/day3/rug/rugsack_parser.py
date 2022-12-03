from typing import List

from src.day3.rug.badge import Badge
from src.day3.rug.rugsack import RugSack


def parse_rugsacks(rows: List[str]) -> List[RugSack]:
    rugs = []
    for row in rows:
        rugs.append(RugSack(row))
    return rugs


def parse_badges(rows: List[str]) -> List[Badge]:
    badges = []
    group = 3
    for row in rows:
        group += 1
        if group == 4:
            group = 1
        if group == 1:
            badge = Badge()
            badges.append(badge)
        badge.add(row)
    return badges


def value_converter(a: str) -> int:
    value = 0
    for letter in a:
        if letter.isupper():
            value += ord(letter) - 38
        else:
            value += ord(letter) - 96
    return value
