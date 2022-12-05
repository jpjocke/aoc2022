from src.day5.stacks.stack_parser import parse_stacks
from src.util.file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day5_in.txt")
stacks = parse_stacks(data)
stacks.print()
stacks.run_instructions()
print(f"problem1: {stacks.get_code()}")

print(f"problem2: {2}")
