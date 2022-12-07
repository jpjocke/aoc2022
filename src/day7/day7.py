import time

from src.day7.file_system.file_system_parser import FileSystemParser
from src.day7.file_system.file_system_traverser import find_total_size_for_problem_1, find_size_delete_for_problem_2
from src.util.file_reader import FileReader

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day7_in.txt")
fs_parser = FileSystemParser()
root = fs_parser.parse_file_system(data)
root.print()
total_size = find_total_size_for_problem_1(root=root)
print(f"problem1: {total_size}")

delete_size = find_size_delete_for_problem_2(root=root)
print(f"problem2: {delete_size}")

print("--- %s seconds ---" % (time.time() - start_time))
