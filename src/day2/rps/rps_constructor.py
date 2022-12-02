from typing import List, Tuple

from src.day2.rps.rps import RPS, ROCK, PAPER, SCISSOR

_MAP = {"A": ROCK, "B": PAPER, "C": SCISSOR, "X": ROCK, "Y": PAPER, "Z": SCISSOR}
_MAP_L = {"A": SCISSOR, "B": ROCK, "C": PAPER}
_MAP_D = {"A": ROCK, "B": PAPER, "C": SCISSOR}
_MAP_W = {"A": PAPER, "B": SCISSOR, "C": ROCK}


def parse_rps(rows: List[str]) -> List[Tuple[RPS, RPS]]:
    ret = []
    for row in rows:
        split = row.split(" ")
        a = RPS(type=_MAP[split[0]])
        b = RPS(type=_MAP[split[1]])
        ret.append((a, b))
    return ret


def parse_rps_2(rows: List[str]) -> List[Tuple[RPS, RPS]]:
    ret = []
    for row in rows:
        split = row.split(" ")
        a = RPS(type=_MAP[split[0]])
        if split[1] == "X":
            b = RPS(type=_MAP_L[split[0]])
        elif split[1] == "Y":
            b = RPS(type=_MAP_D[split[0]])
        else:
            b = RPS(type=_MAP_W[split[0]])
        ret.append((a, b))
    return ret


def count_score(rpss: List[Tuple[RPS, RPS]]) -> int:
    score = 0
    for a, b in rpss:
        score += b.score(a)

    return score
