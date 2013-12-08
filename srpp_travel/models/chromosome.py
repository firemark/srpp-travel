from numpy.random import randint
from numpy import array, insert, arange, append
from ..utils import compute_distance
from types import placedt
from ..cfuns import crossover_fill
from numpy import array, argwhere, split


class Chromosome(object):
    genes = []
    value = -1.0
    magazine = None
    places_in_row = None

    def __init__(self, genes, magazine, places_in_row):
        self.genes = genes
        self.magazine = magazine
        self.places_in_row = places_in_row

    def evaluate(self):
        self.value = compute_distance(
            routes=self.to_routes_with_magazine()["cor"]
        )

        return self.value

    def to_routes_with_magazine(self):
        cors = self.genes
        magazine = self.magazine
        k = self.places_in_row
        len_cors = len(cors)

        cors = insert(cors, arange(len_cors // k + 1) * k, magazine)
        return append(cors, magazine)

    def mutate(self):
        g = self.genes
        len_g = len(g) - 1
        gen_a, gen_b = randint(0, len_g), randint(0, len_g)
        g[gen_b], g[gen_a] = g[gen_a], g[gen_b]
        exit()

    def crossover(self, other):
        """ A x B -> new chromosome """
        genes = self.genes
        other_genes = other.genes
        len_genes = len(genes)

        a = randint(0, len_genes - 3)
        b = randint(a + 1, len_genes - 1)
        genes_range = slice(a, b)

        new_genes = array((-1, (-1, -1)), dtype=placedt).repeat(len_genes)
        new_genes[genes_range] = other_genes[genes_range]
        crossover_fill(new_genes, genes)

        return Chromosome(new_genes, self.magazine, self.places_in_row)

    def print_result(self):
        routes = self.to_routes_with_magazine()["index"]
        # http://stackoverflow.com/questions/5274243/
        splited = split(routes, argwhere(routes == 0))[1:-1]

        print self.value
        print len(splited)

        for route in splited:
            print " ".join(str(i) for i in route), 0
