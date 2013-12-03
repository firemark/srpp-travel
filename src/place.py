from math import sqrt

class Place(object):
    coordinates = None

    def __init__(self, x, y):
    	self.coordinates = []
        self.coordinates.append(x)
        self.coordinates.append(y)

    def __str__(self): return str(self.coordinates)

    def distance(self, another_place):
        return sqrt(sum((ea - eb)**2 for ea, eb in zip(self.coordinates, another_place.coordinates)))