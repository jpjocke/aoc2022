from typing import List, Tuple

from src.day2.rps.rps import RPS, ROCK, PAPER, SCISSOR

_MAP = {"A": ROCK, "B": PAPER, "C": SCISSOR, "X": ROCK, "Y": PAPER, "Z": SCISSOR}


def parse_rps(rows: List[str]) -> List[Tuple[RPS, RPS]]:
    l = []
    for row in rows:
        split = row.split(" ")
        a = RPS(type=_MAP[split[0]])
        b = RPS(type=_MAP[split[1]])
        l.append((a, b))
    return l


def count_score(rpss: List[Tuple[RPS, RPS]]) -> int:
    score = 0
    for a, b in rpss:
        score += b.score(a)

    return score
