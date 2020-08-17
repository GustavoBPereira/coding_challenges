import unittest

from main import comprehensions

class TestField(unittest.TestCase):
    def setUp(self):
        self.possibilities = comprehensions(1, 1, 1, 2)
        self.expected = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

    def test_return_list(self):
        self.assertEqual(list, type(self.possibilities))

    def test_0_0_0(self):
        self.assertIn([0, 0, 0], self.possibilities)

    def test_0_0_1(self):
        self.assertIn([0, 0, 1], self.possibilities)

    def test_0_1_0(self):
        self.assertIn([0, 1, 0], self.possibilities)

    def test_not_0_1_1(self):
        self.assertNotIn([0, 1, 1], self.possibilities)

    def test_1_1_1(self):
        self.assertIn([1, 1, 1], self.possibilities)

    def test_full_output(self):
        self.assertEqual(self.possibilities, self.expected)
