from typing import List

from src.day11.monkey.monkey import Monkey
from src.day11.monkey.operation import Operation


def parse_monkeys(data: str) -> List[Monkey]:
    monkeys = []
    for row in data:
        if len(row) == 0:
            continue
        split = row.split(" ")
        # print(split)
        if split[0] == "Monkey":
            m = Monkey()
            monkeys.append(m)
        elif split[2] == "Starting":
            nrs = split[4:]
            # print(nrs)
            for nr in nrs:
                m.add_item(int(nr.replace(",", "")))
        elif split[2] == "Operation:":
            op = Operation()
            op.op = f"{split[5]} {split[6]} {split[7]}"
            # print(op.op)
            m.op = op
        elif split[2] == "Test:":
            m.test = int(split[5])
            # print(m.test)
        elif split[5] == "true:":
            m.on_true = int(split[9])
            # print(m.on_true)
        elif split[5] == "false:":
            m.on_false = int(split[9])
            # print(m.on_false)
        else:
            raise BaseException(f"unknown line: {row}")

    return monkeys
