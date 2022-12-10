import unittest

from src.day10.cpu.cpu import Cpu
from src.util.file_reader import FileReader


class TestDayTen(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day10_test_in.txt")
        cpu = Cpu()
        cpu.run(data)
        self.assertEqual(13140, cpu.signal_strength)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day10_test_in.txt")
        cpu = Cpu()
        cpu.run(data)
        print(cpu.draw)
        cpu.print_draw()
        self.assertEqual(36, 36)


if __name__ == '__main__':
    unittest.main()
