#!/usr/bin/python3
""" test for class Rectangle """
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ test for class Rectangle"""

    def test_init(self):
        """ test initialization """
        rect = Rectangle(10, 20, 0, 0)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_area(self):
        """ test area"""
        rect = Rectangle(10, 20, 0, 0)
        self.assertEqual(rect.area(), 200)

    def test_display(self):
        """test display"""
        rect = Rectangle(10, 20, 0, 0)
        rect.display()

        expected_output = """
###
###
###
###
###
"""
        self.assertEqual(expected_output, output)

    def test_update(self):
        """test update"""
        rect = Rectangle(10, 20, 0, 0)
        rect.update(width=30, height=40, x=10, y=10)
        self.assertEqual(rect.width, 30)
        self.assertEqual(rect.height, 40)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 10)

    def test_to_dictionary(self):
        """test to_dictionary"""
        rect = Rectangle(10, 20, 0, 0)
        dictionary = rect.to_dictionary()
        self.assertEqual(dictionary['width'], 10)
        self.assertEqual(dictionary['height'], 20)
        self.assertEqual(dictionary['x'], 0)
        self.assertEqual(dictionary['y'], 0)

    def test_negative_values(self):
        """ test negative values"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 20, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, -20, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -10, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 0, -10)


if __name__ == '__main__':
    unittest.main()
