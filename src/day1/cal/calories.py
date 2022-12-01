from typing import List


class Calories:
    c: List[int]

    def __init__(self):
        self.c = []

    def add_c(self, c: int):
        self.c.append(c)

    def sum(self) -> int:
        return sum(self.c)
