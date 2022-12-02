from src.day2.rps.rps_constructor import parse_rps, count_score
from src.util.file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day2_in.txt")
rpss = parse_rps(data)
score = count_score(rpss)
print(f"problem1: {score}")

print(f"problem2: {1}")
