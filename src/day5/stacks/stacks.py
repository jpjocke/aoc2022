from typing import List

from src.day5.stacks.instruction import Instruction


class Stacks:
    stacks: List[List[str]]
    instructions: List[Instruction]

    def __init__(self, stack_size: int):
        self.stacks = []
        self.instructions = []
        for i in range(stack_size):
            self.stacks.append([])

    def add_on_top(self, item: str, stack: int):
        self.stacks[stack].insert(0, item)

    def add_instruction(self, ins: Instruction):
        self.instructions.append(ins)

    def run_instructions(self):
        for ins in self.instructions:
            for i in range(ins.amount):
                item = self.stacks[ins.fr].pop()
                self.stacks[ins.to].append(item)

    def run_instructions_2(self):
        for ins in self.instructions:
            move_list = []
            for i in range(ins.amount):
                item = self.stacks[ins.fr].pop()
                move_list.insert(0, item)
            self.stacks[ins.to].extend(move_list)

    def get_code(self) -> str:
        sb = ""
        for stack in self.stacks:
            sb += stack[-1]
        return sb

    def print(self):
        print("--")
        for stack in self.stacks:
            print(stack)
        print("--")
        for ins in self.instructions:
            print(f"{ins.amount} {ins.fr} {ins.to}")
