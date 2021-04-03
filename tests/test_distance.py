from unittest import TestCase
from cli.models.location import Location
from math import isclose

class TestDistance(TestCase):
    def test_equality_two_equal_objects(self):
        berlin = Location(52.5067614,13.2846508)
        leipzig = Location(51.341699,12.2535538)
        distance = Location.get_distance(berlin, leipzig)
        
        acceptable_error_km = 5
        expected_distance = 149.7 # https://www.distancefromto.net/
        
        actual_error_km = abs(expected_distance - distance)

        self.assertLess(actual_error_km, acceptable_error_km)
