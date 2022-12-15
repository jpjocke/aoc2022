import time

from src.day15.sensor.sensor_map import check_coverage
from src.day15.sensor.sensor_parser import parse_sensors
from src.util.file_reader import FileReader

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day15_in.txt")
sensors = parse_sensors(data)
count = check_coverage(sensors=sensors, row=2000000)
print(f"problem1: {count}")

print(f"problem2: {2}")

print("--- %s seconds ---" % (time.time() - start_time))
