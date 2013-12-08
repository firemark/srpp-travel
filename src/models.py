from os.path import basename
from sys import stdout
from random import randint
from misc import distance
from math import sqrt

# NIE ZMIENIAJ TEGO ZNOWU NA KROTKI. IT WORKS.


class Place(object):
    coordinates = None
    number = None

    def __init__(self, x, y, number):
        self.coordinates = []
        self.coordinates.append(x)
        self.coordinates.append(y)
        self.number = number

    def __str__(self):
        return str(self.coordinates)

    # 40 sekund wykonywania sie dla population 25, iterations 250
    # def distance(self, another_place):
    # return sqrt(sum((ea - eb) ** 2 for ea, eb in zip(self.coordinates,
    # another_place.coordinates)))

    # 15 sekund wykonywania sie dla population 25, iterations 250
    def distance(self, another):
        return sqrt((self.coordinates[0] - another.coordinates[0]) ** 2 + (self.coordinates[1] - another.coordinates[1]) ** 2)


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
            counter = 0
            for line in f:
                row = line.split()
                world.cities.append(Place(int(row[0]), int(row[1]), counter))
                counter += 1

        return world
