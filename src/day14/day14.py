import time

from src.day14.cavern.cavern_parser import parse_cavern
from src.util.file_reader import FileReader
from src.util.point import Point

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day14_in.txt")
cavern = parse_cavern(data)
count = cavern.fill_sand(from_p=Point(x=500, y=0))
print(f"problem1: {count}")

cavern_2 = parse_cavern(data)
cavern_2.fill_floor()
count_2 = cavern_2.fill_sand(from_p=Point(x=500, y=0))
print(f"problem2: {count_2}")

print("--- %s seconds ---" % (time.time() - start_time))
