import time

from src.day13.packets.packet_checker import check_packets, sort_two
from src.day13.packets.packet_parser import parse_packets, parse_packets_2
from src.util.file_reader import FileReader

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day13_in.txt")

packets = parse_packets(data)
count = check_packets(packets)
print(f"problem1: {count}")

packets_l = parse_packets_2(data)
decoder_key = sort_two(packets_l)
print(f"problem2: {decoder_key}")

print("--- %s seconds ---" % (time.time() - start_time))
