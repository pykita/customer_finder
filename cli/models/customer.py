from cli.models.location import Location
from json import dumps

class Customer:
    def __init__(self, latitude, longitude, user_id, name):
        self.location = Location(latitude, longitude)
        self.user_id = user_id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.location == other.location and \
                self.user_id == other.user_id and \
                self.name == other.name
        return False
        

    # def to_json(self):
    #     d = {
    #         'latitude': self.location.latitude,
    #         'longitude': self.location.longitude,
    #         'user_id': self.user_id,
    #         'name': self.name
    #     }

    #     return dumps(d)