from os.path import basename
from sys import stdout
from random import randint
from misc import distance
from math import sqrt

# NIE ZMIENIAJ TEGO ZNOWU NA KROTKI. IT WORKS.


class Place(object):
    coordinates = None
    number = None

    def __init__(self, number, cor):
        self.coordinates = (cor[0], cor[1])
        self.number = number

    def __iter__(self):
        return iter(self.coordinates)

    def __str__(self):
        return str(self.coordinates)

    # 15 sekund wykonywania sie dla population 25, iterations 250
    def distance(self, another):
        return sqrt((self.coordinates[0] - another.coordinates[0]) ** 2 +
                   (self.coordinates[1] - another.coordinates[1]) ** 2)


class Chromosome(object):
    genes = []
    value = -1.0
    magazine = None
    places_in_row = None

    def __init__(self, genes, magazine, places_in_row):
        self.genes = genes
        self.magazine = magazine
        self.places_in_row = places_in_row


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

    # PRZEROBILEM, TERAZ DZIALA.
    @staticmethod
    def from_file(path):
        world = World()
        world.filename = basename(path)
        with open(path) as f:
            world.k = int(f.readline())
            for i, line in enumerate(f):
                row = [int(i) for i in line.split()]
                world.cities.append(Place(i, row))

        return world


class Result(object):

    world = None
    routes = None
    length = -1.0

    def __init__(self, world):
        self.world = world
        self.routes = []

    def add_route(self, route):
        if len(route) > self.world.k + 2:
                raise Exception("Route is too big")
        self.routes.append(route)

    def add_route_with_magazine(self, route):
        self.add_route([0] + route + [0])

    def validate(self):
        """raise exceptions if have any errors"""
        routes_set = set()

        for i, route_set in enumerate(set(r) for r in self.routes):
            res = route_set & routes_set - {0}
            if res:
                raise Exception("repeated indexes %s in %d route" % (res, i))
            routes_set |= route_set

    # TODO FIREMARK. NIE DZIALA
    def compute_length(self):
        """compute distance, save to self.length and return"""
        self.validate()

        length = 0.0
        cities = self.world.cities

        for route in self.routes:
            prev_city = route[0]
            for city in route[1:]:
                length += distance(cities[city], cities[prev_city])
                prev_city = city

        self.length = length
        return length

    # def print_result(self, stream=stdout):
    #     print self.world.cities
    #     if self.length < 0.0:
    #         self.compute_length()

    #     stream.write("%f\n" % self.length)
    #     stream.write("%d\n" % len(self.routes))

    #     for route in self.routes:
    #         stream.write(" ".join(str(i) for i in route) + "\n")

    # FUNKCJA-PROTOTYP, DO DEBUGU ALGORYTMU. POZNIEJ WYSWIETLISZ SOBIE JAK
    # CHCESZ
    def print_result(self, stream=stdout):
        print self.length
        counter = -1
        for place in self.world.cities:
            print place
            counter += 1
            if counter == 5:
                counter = 0
                print self.world.cities[0]
