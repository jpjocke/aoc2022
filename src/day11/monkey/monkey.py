import math
from typing import List

from src.day11.monkey.operation import Operation


class Monkey:
    items: List[int]
    test: int
    op: Operation
    on_true: int
    on_false: int
    inspections: int

    def __init__(self):
        self.items = []
        self.inspections = 0

    def add_item(self, item: int):
        self.items.append(item)

    def inspect_items(self, monkeys: List["Monkey"]):
        while len(self.items) > 0:
            item = self.items.pop(0)
            item = self.op.calc_new_level(item)
            item = math.floor(item / 3)
            if item % self.test == 0:
                monkeys[self.on_true].add_item(item)
            else:
                monkeys[self.on_false].add_item(item)
            self.inspections += 1
