import time

from src.day8.forest.forest import Forest
from src.util.file_reader import FileReader

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day8_in.txt")
forest = Forest(data=data)
visible = forest.find_visible()
print(f"problem1: {visible}")

scenic = forest.find_scenic()
print(f"problem2: {scenic}")

print("--- %s seconds ---" % (time.time() - start_time))
