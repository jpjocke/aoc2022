from typing import Set, List

from src.util.point import Point
from src.util.util import get_key_pos


class Rope:
    rope: List[Point]
    visited: Set[str]

    def __init__(self, size: int):
        self.rope = []
        for i in range(size):
            self.rope.append(Point(50, 50))
        self.visited = set()
        self._add_tail_to_visited()

    def _add_tail_to_visited(self):
        last = self.rope[len(self.rope) - 1]
        self.visited.add(get_key_pos(last))

    def count_visited(self) -> int:
        return len(self.visited)

    def run(self, data: List[str]):
        for row in data:
            split = row.split(" ")
            for i in range(int(split[1])):
                self._run_instruction(split[0])

            # print(row)
            # for r in self.rope:
            #     print(r)

    def _run_instruction(self, d: str):
        if d == "R":
            self.rope[0].x += 1
        elif d == "L":
            self.rope[0].x -= 1
        elif d == "U":
            self.rope[0].y -= 1
        else:
            self.rope[0].y += 1

        for i in range(len(self.rope)):
            if i == 0:
                continue
            if self._should_tail_move(i):
                self._move_tail(i)

    def _move_tail(self, index: int):
        if self.rope[index - 1].distance(self.rope[index]) == 2:
            self._move_tail_one_dimension(index)
        elif self.rope[index - 1].distance(self.rope[index]) == 3:
            self._move_tail_two_dimension(index)
        else:
            self._move_tail_long(index)
        self._add_tail_to_visited()

    def _move_tail_one_dimension(self, index: int):
        if self.rope[index - 1].x == self.rope[index].x:
            self.rope[index].y += int((self.rope[index - 1].y - self.rope[index].y) / 2)
        elif self.rope[index - 1].y == self.rope[index].y:
            self.rope[index].x += int((self.rope[index - 1].x - self.rope[index].x) / 2)

    def _move_tail_two_dimension(self, index: int):
        # diff: 2 in one dir and 1 in the other dir
        if abs(self.rope[index - 1].y - self.rope[index].y) > 1:
            self.rope[index].x = self.rope[index - 1].x
        else:
            self.rope[index].y = self.rope[index - 1].y
        self._move_tail_one_dimension(index)

    def _move_tail_long(self, index: int):
        if self.rope[index - 1].y > self.rope[index].y:
            self.rope[index].y = self.rope[index - 1].y - 1
        if self.rope[index - 1].y < self.rope[index].y:
            self.rope[index].y = self.rope[index - 1].y + 1
        if self.rope[index - 1].x > self.rope[index].x:
            self.rope[index].x = self.rope[index - 1].x - 1
        if self.rope[index - 1].x < self.rope[index].x:
            self.rope[index].x = self.rope[index - 1].x + 1

    def _should_tail_move(self, index: int) -> bool:
        if abs(self.rope[index - 1].y - self.rope[index].y) > 1:
            return True
        return abs(self.rope[index - 1].x - self.rope[index].x) > 1
