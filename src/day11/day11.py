import time

from src.day11.monkey.monkey_parser import parse_monkeys
from src.day11.monkey.monkey_runner import run_monkeys
from src.util.file_reader import FileReader

start_time = time.time()
fr = FileReader()
data = fr.read_as_str_lines("../../data/day11_in.txt")
monkeys = parse_monkeys(data)
monkey_business = run_monkeys(monkeys, 20)
print(f"problem1: {monkey_business}")

monkeys = parse_monkeys(data)
monkey_business = run_monkeys(monkeys, 10000, False)
print(f"problem2: {monkey_business}")

print("--- %s seconds ---" % (time.time() - start_time))
