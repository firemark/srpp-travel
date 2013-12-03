from os.path import basename
from sys import stdout
from place import Place


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

    def get_magazine_place(self):
        city = self.cities[0]
        print city[0]
        magazine_place = Place(city[0], city[1])
        return magazine_place

    # get list of place objects, without magazine
    def get_places_list(self):
        places_list = []
        for city in self.cities[1:] :
            place = Place(city[0], city[1])
            places_list.append(place)
        return places_list

    magazine = property(get_magazine, set_magazine)

    @staticmethod
    def from_file(path):
        world = World()
        world.filename = basename(path)
        with open(path) as f:
            world.k = int(f.readline())
            world.cities = [tuple(int(i) for i in line.split()) for line in f]

        return world
