import unittest
from cli.controllers.customer import CustomerController
from cli.config import dublin_location
from cli.models.customer import Customer
from cli.models.location import Location
from unittest.mock import patch, Mock, call

class TestCustomerController(unittest.TestCase):
    def test_get_close_customers(self):
        with patch('cli.controllers.customer.get_customers') as get_customers, \
            patch.object(Location, 'get_distance') as patched_get_distance, \
            patch('cli.controllers.customer.save_customers') as save_customers:
            # patching dependencies
            get_customers.return_value = [
                Customer(1.1111, 2.2222, 1, 'Jack'),
                Customer(3.3333, 4.4444, 2, 'John')
            ]
            patched_get_distance.side_effect = [190,19]

            # call the tested method
            controller = CustomerController()
            controller.get_close_customers('not_a_real_file.txt', 'some_output.txt', 100)

            # assert the correctness
            get_customers.assert_called_with('not_a_real_file.txt')
            expected_get_distance_calls = [
                call(Location(1.1111, 2.2222), dublin_location)
            ]
            
