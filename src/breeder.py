from models import Result, World, Chromosome
from config import mutation_chance_perc, population
from numpy.random import choice, permutation, randint


class Breeder(object):

    chromosomes = None
    chromosomes_new_generation = None

    def __init__(self, world):
        self.chromosomes = []
        self.populate_chromosomes(world)
        self.chromosomes_new_generation = []

    def mutate_chromosomes(self):
        for chromosome in self.chromosomes:
            if randint(1, 100) <= mutation_chance_perc:
                chromosome.mutate()

    def sort_chromosomes_by_value(self):
        self.chromosomes.sort(key=lambda obj: obj.evaluate(), reverse=True)

    def remove_weak_chromosomes(self):
        self.sort_chromosomes_by_value()
        del self.chromosomes[:len(self.chromosomes) // 2]

    def crossover_chromosomes(self):
        size = len(self.chromosomes)
        pair_chromosomes = choice(self.chromosomes, [size // 2, 2],
                                  replace=False)

        self.chromosomes_new_generation = sum(
            (
                [a.crossover(b), b.crossover(a)]
                for a, b in pair_chromosomes
            ), start=[]
        )

    def overwrite_old_generation_with_new(self):
        self.chromosomes = self.chromosomes_new_generation
        self.chromosomes_new_generation = []

    def do_shit(self):
        self.remove_weak_chromosomes()
        # crossover needs to be done two times
        self.crossover_chromosomes()
        self.crossover_chromosomes()
        self.overwrite_old_generation_with_new()
        self.mutate_chromosomes()

    def get_best_chromosome(self):
        self.sort_chromosomes_by_value()
        return self.chromosomes[0]

    def populate_chromosomes(self, world):
        magazine = world.magazine
        places = world.get_places_list()
        places_in_row = world.k

        self.chromosomes = [
            Chromosome(permutation(places), magazine, places_in_row)
            for _ in range(population)
        ]

    def get_result(self):
        chromosome = self.get_best_chromosome()
        world = World()
        world.cities = chromosome.genes
        world.cities.insert(0, chromosome.magazine)

        result = Result(world)

        return result

    def get_result_value(self):
        chromosome = self.get_best_chromosome()
        return chromosome.value
