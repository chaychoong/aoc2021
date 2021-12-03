import unittest

from aoc2021.utils import parse_input_lambda

lambda_inp = lambda x: str(x)

class TestDay3Example(unittest.TestCase):
    def test_day3_example(self):
        from aoc2021.day3.main import day3_solution

        input = parse_input_lambda("example.txt", lambda_inp)
        self.assertEqual(day3_solution(input), 198)

    def test_day3_example_p2(self):
        from aoc2021.day3.main import day3_solution_p2

        input = parse_input_lambda("example.txt", lambda_inp)
        self.assertEqual(day3_solution_p2(input), 230)
