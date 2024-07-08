import unittest
from parameterized import parameterized
from app.main import Calculator
from app.error import InvalidInputException


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def tearDown(self) -> None:
        ...

    @parameterized.expand([
        (10, 2, 3.3219280948873626),
        (100, 10, 2),
        (8, 2, 3),
    ])
    def test_log_valid_input(self, a, base, expected):
        result = self.calc.log(a, base)
        self.assertAlmostEqual(result, expected, places=5)

    @parameterized.expand([
        ("a", 2),
        (10, "b"),
        ("a", "b"),
    ])
    def test_log_invalid_input_type(self, a, base):
        with self.assertRaises(TypeError):
            self.calc.log(a, base)

    @parameterized.expand([
        (0, 2),
        (1, 2),
        (10, 0),
        (-10, 2),
    ])
    def test_log_invalid_input_domain(self, a, base):
        with self.assertRaises(InvalidInputException):
            self.calc.log(a, base)


if __name__ == '__main__':
    unittest.main()