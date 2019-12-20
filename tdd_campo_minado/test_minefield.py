import unittest
from minefield import get_positions


class TestField(unittest.TestCase):
    def setUp(self):
        self.bombs = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [3, 1], [0, 2]]
        self.minefield = get_positions(6, 6, bombs=self.bombs)
        b = '*'
        self.expected_field = [
            [0, 1, b, 1, 2, b],
            [0, 1, 1, 1, 3, b],
            [1, 1, 1, 0, 3, b],
            [1, b, 1, 0, 3, b],
            [1, 1, 1, 0, 3, b],
            [0, 0, 0, 0, 2, b],
        ]

    def test_return_list(self):
        self.assertEqual(list, type(self.minefield))

    def test_locations_with_bombs(self):
        for location in self.bombs:
            self.assertEqual('*', self.expected_field[location[0]][location[1]])

    def test_count_bombs(self):
        bombs = 0
        for line in self.expected_field:
            bombs += line.count('*')
        self.assertEqual(len(self.bombs), bombs)

    def test_locations_without_bombs(self):
        no_bombs = 0
        for line in self.expected_field:
            for column in line:
                if column != '*':
                    no_bombs += 1
        self.assertEqual(28, no_bombs)

    def test_full_camp(self):
        self.assertEqual(self.expected_field, self.minefield)
