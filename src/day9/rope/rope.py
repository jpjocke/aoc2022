from typing import Set, List

from src.util.point import Point
from src.util.util import get_key_pos


class Rope:
    head: Point
    tail: Point
    visited: Set[str]

    def __init__(self):
        self.head = Point(50, 50)
        self.tail = Point(50, 50)
        self.visited = set()
        self._add_tail_to_visited()

    def _add_tail_to_visited(self):
        self.visited.add(get_key_pos(self.tail))

    def count_visited(self) -> int:
        return len(self.visited)

    def run(self, data: List[str]):
        for row in data:
            split = row.split(" ")
            for i in range(int(split[1])):
                self._run_instruction(split[0])

    def _run_instruction(self, d: str):
        if d == "R":
            self.head.x += 1
        elif d == "L":
            self.head.x -= 1
        elif d == "U":
            self.head.y -= 1
        else:
            self.head.y += 1

        if self._should_tail_move():
            self._move_tail()

    def _move_tail(self):
        if self.head.distance(self.tail) == 2:
            self._move_tail_one_dimension()
        elif self.head.distance(self.tail) == 3:
            self._move_tail_two_dimension()
        else:
            raise BaseException("Distance too far")
        self._add_tail_to_visited()

    def _move_tail_one_dimension(self):
        if self.head.x == self.tail.x:
            self.tail.y += int((self.head.y - self.tail.y) / 2)
        elif self.head.y == self.tail.y:
            self.tail.x += int((self.head.x - self.tail.x) / 2)

    def _move_tail_two_dimension(self):
        # diff: 2 in one dir and 1 in the other dir
        if abs(self.head.y - self.tail.y) > 1:
            self.tail.x = self.head.x
        else:
            self.tail.y = self.head.y
        self._move_tail_one_dimension()

    def _should_tail_move(self) -> bool:
        if abs(self.head.y - self.tail.y) > 1:
            return True
        return abs(self.head.x - self.tail.x) > 1
