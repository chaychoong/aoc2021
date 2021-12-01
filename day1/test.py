import unittest

from aoc2021.utils import parse_input


class TestDay1Example(unittest.TestCase):
    def test_day1_example(self):
        from aoc2021.day1.main import day1_solution

        input = parse_input("example.txt")
        self.assertEqual(day1_solution(input), 7)

    def test_day1_example_p2(self):
        from aoc2021.day1.main import day1_solution_p2

        input = parse_input("example.txt")
        self.assertEqual(day1_solution_p2(input), 5)
