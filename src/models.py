from os.path import basename
from misc import distance
from sys import stdout

from place import Place
from breeder import Breeder


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
            world.cities = [Place(int(i) for i in line.split()) for line in f]

        return world


class Result(object):

    world = None
    routes = None
    length = -1.0
    breeder = None

    def __init__(self, world):
        self.world = world
        self.routes = []

    def add_route(self, route):
        self.routes.append(route)

    def add_route_with_magazine(self, route):
        self.add_route([0] + route + [0])

    def compute_length(self):
        """compute distance, save to self.length and return"""
        length = 0
        cities = self.world.cities

        for route in self.routes:
            prev_city = route[0]
            for city in route[1:]:
                length += distance(cities[city], cities[prev_city])
                prev_city = city

        self.length = length
        return length

    def print_result(self, stream=stdout):
        if self.length < 0.0:
            self.compute_length()

        stream.write("%f\n" % self.length)
        stream.write("%d\n" % len(self.routes))

        for route in self.routes:
            stream.write(" ".join(str(i) for i in route) + "\n")
