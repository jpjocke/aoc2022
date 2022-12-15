import unittest

from src.day15.sensor.sensor_map import check_coverage
from src.day15.sensor.sensor_parser import parse_sensors
from src.util.file_reader import FileReader


class TestDayFourteen(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day15_test_in.txt")
        sensors = parse_sensors(data)
        count = check_coverage(sensors=sensors, row=10)
        self.assertEqual(26, count)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day15_test_in.txt")
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
