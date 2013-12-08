from os.path import basename
from types import placedt
from numpy import array


class World(object):
    filename = ""
    k = 0  # maximum cities per route
    cities = None

    def __init__(self):
        self.cities = []

    def get_magazine(self):
        return self.cities[0]

    def set_magazine(self, val):
        self.cities[0] = val

    def get_places_list(self):
        return self.cities[1:]

    magazine = property(get_magazine, set_magazine)

    @staticmethod
    def from_file(path):
        world = World()
        world.filename = basename(path)
        with open(path) as f:
            world.k = int(f.readline())
            world.cities = array([
                (i, [int(num) for num in line.split()])
                for i, line in enumerate(f)
            ], dtype=placedt)

        return world
