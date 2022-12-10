import time

from src.day10.cpu.cpu import Cpu
from src.util.file_reader import FileReader

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day10_in.txt")
cpu = Cpu()
cpu.run(data)
print(f"problem1: {cpu.signal_strength}")

cpu.print_draw()
print(f"problem2: {2}")

print("--- %s seconds ---" % (time.time() - start_time))
