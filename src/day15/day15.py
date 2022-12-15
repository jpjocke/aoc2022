import time

from src.day15.sensor.sensor_map import BeaconFinder
from src.day15.sensor.sensor_parser import parse_sensors
from src.util.file_reader import FileReader

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day15_in.txt")
sensors = parse_sensors(data)
# count = check_coverage(sensors=sensors, row=2000000)
# print(f"problem1: {count}")
bf = BeaconFinder(sensors=sensors, max_size=4000000)
beacon = bf.find()

print(f"problem2: {beacon}")

print("--- %s seconds ---" % (time.time() - start_time))
