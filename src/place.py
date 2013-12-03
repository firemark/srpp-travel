from misc import distance


class Place(object):
    coordinates = None

    def __init__(self, *cor):
        self.coordinates = cor

    def __iter__(self):
        return iter(self.coordinates)

    def distance(self, another_place):
        return distance(self, another_place)
