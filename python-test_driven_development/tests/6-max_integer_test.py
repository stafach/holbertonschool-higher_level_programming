#!/usr/bin/python3
"""Unittests for max_integer([..]).
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for the function max_integer."""

    def test_ordered_list(self):
        """Max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Empty list should return None."""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """A single-element list should return that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """List with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """List with both positive and negative numbers."""
        self.assertEqual(max_integer([-10, -5, 0, 5, 10]), 10)

    def test_floats(self):
        """List with floats."""
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 2.8]), 3.9)

    def test_string(self):
        """String input should return max char (lexicographically)."""
        self.assertEqual(max_integer("hello"), 'o')

    def test_list_of_strings(self):
        """List of strings returns max string lexicographically."""
        self.assertEqual(max_integer(["abc", "xyz", "def"]), "xyz")


if __name__ == '__main__':
    unittest.main()
