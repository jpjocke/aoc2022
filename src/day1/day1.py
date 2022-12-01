from src.day1.cal.calories_builder import build_c, find_highest, find_top_three_sum
from src.util.file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day1_in.txt")

cs = build_c(data)
for c in cs:
    print(c.sum())
print("")
max_c = find_highest(cs)
print(f"problem1: {max_c.sum()}")

sum_3 = find_top_three_sum(cs)
print(f"problem2: {sum_3}")