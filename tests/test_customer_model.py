from unittest import TestCase
from cli.models.customer import Customer
from cli.models.location import Location

class TestCustomer(TestCase):
    def test_equality_two_equal_objects(self):
        first = Customer(1.1111, 2.2222, 1, 'James Smith')
        second = Customer(1.1111, 2.2222, 1, 'James Smith')

        self.assertEqual(first, second)

    def test_equality_two_objects_of_diff_type(self):
        first = Customer(1.1111, 2.2222, 1, 'James Smith')
        second = Location(1.1111, 2.2222)

        self.assertNotEqual(first, second)

    def test_equality_two_diff_customers(self):
        first = Customer(1.1111, 2.2222, 1, 'James Smith')
        second = Customer(3.3333, 4.4444, 2, 'Jack Reacher')

        self.assertNotEqual(first, second)