import unittest

from aoc2021.utils import parse_input


class TestDay2Example(unittest.TestCase):
    def test_day2_example(self):
        from aoc2021.day2.main import day2_solution

        input = parse_input("example.txt")
        self.assertEqual(day2_solution(input), 150)

    def test_day2_example_p2(self):
        from aoc2021.day2.main import day2_solution_p2

        input = parse_input("example.txt")
        self.assertEqual(day2_solution_p2(input), 900)
