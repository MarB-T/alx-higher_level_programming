#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ testing Base """
    def test_no_args(self):
        """no argument test"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_id(self):
        """test with id"""
        b1 = Base(10)
        self.assertEqual(b1.id, 11)

    def test_get_instance(self):
        """assurance that instance cannot be get"""
        with self.assertRaises(AttributeError):
            print(Base().__nb_instances)

    def test_none_instance(self):
        """test for None instance"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_for_list(self):
        """list"""
        self.assertEqual([1, 2, 3, 4], Base([1, 2, 3, 4]).id)

    def test_for_dict(self):
        """dict"""
        self.assertEqual({'a': 2, 'b': 1}, Base({'a': 2, 'b': 1}).id)

    def test_for_complex(self):
        """complex"""
        self.assertEqual(complex(10), Base(complex(10)).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()
