import unittest

from src.day13.packets.packet_checker import check_packets, sort_two
from src.day13.packets.packet_parser import parse_packets, parse_packets_2
from src.util.file_reader import FileReader


class TestDayThirteen(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day13_test_in.txt")
        packets = parse_packets(data)
        count = check_packets(packets)
        self.assertEqual(13, count)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day13_test_in.txt")
        packets_l = parse_packets_2(data)
        decoder_key = sort_two(packets_l)
        self.assertEqual(140, decoder_key)


if __name__ == '__main__':
    unittest.main()
