import time

from src.day9.rope.rope import Rope
from src.util.file_reader import FileReader

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day9_in.txt")
rope = Rope(2)
rope.run(data)
visited = rope.count_visited()
print(f"problem1: {visited}")
rope = Rope(10)
rope.run(data)
visited = rope.count_visited()

print(f"problem2: {visited}")

print("--- %s seconds ---" % (time.time() - start_time))
