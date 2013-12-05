from numpy.random import choice
from numpy import split
from utils import compute_distance_with_magazine


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
        self.value = compute_distance_with_magazine(
            places=self.as_matrix(),
            magazine=self.magazine,
        )

        return self.value

    def as_matrix(self):
        genes = self.genes
        return split(genes, len(genes) // self.places_in_row)

    def mutate(self):
        g = self.genes
        gen_a, gen_b = choice(len(g), 2)
        g[gen_b], g[gen_a] = g[gen_a], g[gen_b]

    def crossover(self, other):
        """ A x B -> new chromosome """
        new_genes = self.genes.copy()

        return Chromosome(new_genes, self.magazine, self.places_in_row)
