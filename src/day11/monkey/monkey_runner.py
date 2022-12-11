from typing import List

from src.day11.monkey.monkey import Monkey


def run_monkeys(monkeys: List[Monkey], runs: int) -> int:
    for i in range(runs):
        for m in monkeys:
            m.inspect_items(monkeys)
    ins = [m.inspections for m in monkeys]
    ins.sort()
    ins_top = ins[-2::]
    print(ins_top)
    return ins_top[0] * ins_top[1]
