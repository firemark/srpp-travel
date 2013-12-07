from os.path import basename
from sys import stdout
from types import placedt
from numpy import array
from ..utils import add_magazine, compute_distance


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


class Result(object):

    routes = None
    distance = -1.0

    def __init__(self, routes, magazine):
        self.routes = add_magazine(routes, magazine)

    def validate(self):
        """raise exceptions if have any errors"""
        routes_set = set()

        for i, route_set in enumerate(set(r) for r in self.routes):
            res = (route_set - {0}) & routes_set
            if res:
                raise Exception("repeated indexes %s in %d route" % (res, i))
            routes_set |= route_set

    def compute_distance(self):
        """compute distance, save to self.length and return"""
        self.validate()
        self.distance = compute_distance(self.routes)
        return self.distance

    def print_result(self, stream=stdout):
        if self.distance < 0.0:
            self.compute_distance()

        print >> stream, self.distance
        print >> stream, len(self.routes)

        for route in self.routes:
            print >> stream, " ".join(str(i) for i in route["index"]), 0
