import time

from src.day13.packets.packet_checker import check_packets
from src.day13.packets.packet_parser import parse_packets
from src.util.file_reader import FileReader

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day13_in.txt")

packets = parse_packets(data)
count = check_packets(packets)
print(f"problem1: {count}")

print(f"problem2: {2}")

print("--- %s seconds ---" % (time.time() - start_time))
