from src.day4.section.sections_parser import parse_sections, count_fits
from src.util.file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day4_in.txt")
sections_list = parse_sections(data)
count = count_fits(sections_list)
print(f"problem1: {count}")

print(f"problem2: {2}")
