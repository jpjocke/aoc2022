import unittest

from src.day15.sensor.sensor_map import check_coverage, BeaconFinder
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
        sensors = parse_sensors(data)
        bf = BeaconFinder(sensors=sensors, max_size=20)
        beacon = bf.find()
        self.assertEqual(beacon, 56000011)


if __name__ == '__main__':
    unittest.main()
