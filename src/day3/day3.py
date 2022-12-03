from src.day3.rug.rugsack_parser import parse_rugsacks, value_converter, parse_badges
from src.util.file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day3_in.txt")
rugs = parse_rugsacks(data)
total = 0
for rug in rugs:
    dup = rug.find_duplicates()
    total += value_converter(dup)
print(f"problem1: {total}")


badges = parse_badges(data)
total_b = 0
for b in badges:
    total_b += value_converter(b.find_badge())
print(f"problem2: {total_b}")
