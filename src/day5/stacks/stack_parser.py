from typing import List, Tuple

from src.day5.stacks.instruction import Instruction
from src.day5.stacks.stacks import Stacks


def parse_stacks(rows: List[str]) -> Stacks:
    stack_size, size = _find_stack_size_rows(rows)
    print(stack_size)
    stacks = Stacks(stack_size=stack_size)
    stack_mode = True
    for row in rows:
        if len(row) == 0:
            stack_mode = False
            continue
        if stack_mode:
            if "[" in row:
                _parse_stack_row(row, size, stacks)
        else:
            _parse_instruction(row, stacks)
    return stacks


def _parse_stack_row(row: str, size: int, stacks: Stacks):
    print(row)
    place = 1
    stack_place = 0
    try:
        while place < size:
            if row[place] != " ":
                stacks.add_on_top(row[place], stack_place)
            place += 4
            stack_place += 1
    except IndexError:
        # Some kind of error where the last spaces is not read in correctly at end of line
        pass


def _find_stack_size_rows(rows: List[str]) -> Tuple[int, int]:
    for i, row in enumerate(rows):
        if len(row) == 0:
            size = len(rows[i - 2])
            return _find_stack_size(size), size


def _find_stack_size(size: int) -> int:
    place = 1
    stack_size = 0
    while place < size:
        place += 4
        stack_size += 1
    return stack_size


def _parse_instruction(row: str, stacks: Stacks):
    split = row.split(" ")
    ins = Instruction(amount=int(split[1]), fr=int(split[3]) - 1, to=int(split[5]) - 1)
    stacks.add_instruction(ins)
