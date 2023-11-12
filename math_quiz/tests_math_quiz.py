import unittest
from math_quiz import randInt, randOper, generateProblem


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randInt(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        for _ in range(1000):
             output = randOper()
             self.assertTrue(output in ['+', '-', '*'])
        pass

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 3, '-', '4 - 3', 1),
                (6, 8, '*', '6 + 8', 48),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                tmp_prob, tmp_ans = generateProblem(num1,num2,operator)
                self.assertTrue(tmp_ans == expected_answer and tmp_prob == expected_problem)

if __name__ == "__main__":
    unittest.main()


