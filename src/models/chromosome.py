from numpy.random import choice, randint
from numpy import array_split, in1d
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
            routes=self.to_routes(),
            magazine=self.magazine,
        )

        return self.value

    def to_routes(self):
        genes = self.genes
        return array_split(genes, len(genes) // self.places_in_row)

    def mutate(self):
        g = self.genes
        gen_a, gen_b = choice(len(g), 2)
        g[gen_b], g[gen_a] = g[gen_a], g[gen_b]

    def crossover(self, other):
        """ A x B -> new chromosome """
        new_genes = self.genes.copy()
        other_genes = other.genes
        len_genes = len(self.genes)

        a = randint(0, len_genes - 2)
        b = randint(a, len_genes - 1)

        genes_range = slice(a, b)
        sliced_other_genes = other_genes[genes_range]
        sliced_new_genes = new_genes[genes_range]

        mask = in1d(new_genes["index"], sliced_other_genes["index"])
        new_genes[mask] = sliced_new_genes
            
        sliced_new_genes = sliced_other_genes

        return Chromosome(new_genes, self.magazine, self.places_in_row)
