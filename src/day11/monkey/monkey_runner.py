from typing import List

from src.day11.monkey.monkey import Monkey


def run_monkeys(monkeys: List[Monkey], runs: int, use_worry_level: bool = True) -> int:
    for i in range(runs):
        for m in monkeys:
            m.inspect_items(monkeys, use_worry_level)
    ins = [m.inspections for m in monkeys]
    ins.sort()
    ins_top = ins[-2::]
    return ins_top[0] * ins_top[1]
