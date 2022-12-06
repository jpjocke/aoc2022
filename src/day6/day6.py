import time

from src.day6.buffer.signal_finder import find_start_of_packet, find_start_of_message
from src.util.file_reader import FileReader

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day6_in.txt")
packet_start = find_start_of_packet(data[0])
print(f"problem1: {packet_start}")

message_start = find_start_of_message(signal=data[0], start=packet_start)
print(f"problem2: {message_start}")

print("--- %s seconds ---" % (time.time() - start_time))
