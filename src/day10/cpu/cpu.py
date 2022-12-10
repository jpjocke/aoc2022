from typing import List


class Cpu:
    x: int
    cycle: int
    signal_strength: int
    draw: List[str]

    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.signal_strength = 0
        self.draw = []

    def run(self, data: List[str]):
        for row in data:
            split = row.split(" ")
            if split[0] == "noop":
                self._increase_cycle()
            elif split[0] == "addx":
                self._increase_cycle()
                self._increase_cycle()
                self.x += int(split[1])
            else:
                raise BaseException("Unknown command")

    def _increase_cycle(self):
        draw_pos = self.cycle % 40
        if self.x - 1 <= draw_pos <= self.x + 1:
            self.draw.append("#")
        else:
            self.draw.append(".")
        self.cycle += 1
        if (self.cycle - 20) % 40 == 0:
            ss = self.cycle * self.x
            self.signal_strength += ss

    def print_draw(self):
        sb = ""
        char = 0
        for c in self.draw:
            sb += c
            char += 1
            if char % 40 == 0:
                print(sb)
                sb = ""
                char = 0
