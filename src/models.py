from os.path import basename


class World(object):
    filename = ""
    k = 0  # maximum cities per route
    cities = []

    def get_magazine(self):
        return self.cities[0]

    def set_magazine(self, val):
        self.cities[0] = val

    magazine = property(get_magazine, set_magazine)

    @staticmethod
    def from_file(path):
        world = World()
        world.filename = basename(path)
        with open(path) as f:
            world.k = int(f.readline())
            world.cities = [tuple(int(i) for i in line.split()) for line in f]

        return world
