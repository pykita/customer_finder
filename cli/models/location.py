from math import radians, sin, cos, acos

class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.latitude == other.latitude and \
                self.longitude == other.longitude
        return False

    @staticmethod
    def get_distance(first_loc, second_loc):
        '''
            Returns distance between two locations:
            the current and the one passed. Distance is in km.
            The geometrical formulas are taken from 
            https://en.wikipedia.org/wiki/Great-circle_distance#Radius_for_spherical_Earth
        '''
        earth_radius = 6371.009

        delta_long = radians(abs(second_loc.longitude - first_loc.longitude))
        first_rad_lat = radians(first_loc.latitude)
        second_rad_lat = radians(second_loc.latitude)

        central_angle = acos(sin(first_rad_lat) * sin(second_rad_lat) + \
            cos(first_rad_lat) * cos(second_rad_lat) * cos(delta_long)
        )

        distance = central_angle * earth_radius

        return distance