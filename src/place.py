from math import sqrt

class Place(object):
	coordinates = []

	def __init__(self, x, y):
        self.coordinates[0] = x
        self.coordinates[1] = y

    def distance(self, another_place):
    	return sqrt(sum((ea - eb)**2 for ea, eb in zip(self.coordinates, another_place.coordinates)))