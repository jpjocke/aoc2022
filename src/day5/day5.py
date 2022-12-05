from src.day5.stacks.stack_parser import parse_stacks
from src.util.file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day5_in.txt")
stacks = parse_stacks(data)
stacks.run_instructions()
print(f"problem1: {stacks.get_code()}")

stacks_2 = parse_stacks(data)
stacks_2.run_instructions_2()
print(f"problem2: {stacks_2.get_code()}")
