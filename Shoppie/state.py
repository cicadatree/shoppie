from location import Location
from items import Items

class State:
    def __init__(self, location: Location, items: Items):
        self.location = location
        self.items = items
        return 
    