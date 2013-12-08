from chromosome import Chromosome
from ..config import mutation_chance_perc, population
from numpy.random import random, permutation, shuffle
from numpy import array, argwhere, split
from sys import stdout


class Breeder(object):

    chromosomes = None
    chromosomes_new_generation = None

    def __init__(self, world):
        self.chromosomes = []
        self.populate_chromosomes(world)
        self.chromosomes_new_generation = []

    def mutate_chromosomes(self):
        for chromosome in self.chromosomes:
            if random <= mutation_chance_perc:
                chromosome.mutate()

    def sort_chromosomes_by_value(self):
        self.chromosomes.sort(key=Chromosome.evaluate)

    def remove_weak_chromosomes(self):
        self.sort_chromosomes_by_value()
        del self.chromosomes[len(self.chromosomes) // 2:]

    def crossover_chromosomes(self):
        chromosomes = self.chromosomes
        half_size = len(chromosomes) // 2

        # only even
        pair_chromosomes = array(chromosomes[:half_size * 2])
        shuffle(pair_chromosomes)

        # group [a,b,c,d...] to [(a,b), (c,d)]
        pair_chromosomes.shape = (half_size, 2)

        self.chromosomes_new_generation += sum(
            (
                [a.crossover(b), b.crossover(a)]
                for a, b in pair_chromosomes
            ), []
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

    def get_winner(self):
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

    def print_result(self, stream=stdout):

        winner = self.get_winner()
        routes = winner.to_routes_with_magazine()["index"]
        # http://stackoverflow.com/questions/5274243/
        splited = split(routes, argwhere(routes == 0))[1:-1]

        print >> stream, winner.value
        print >> stream, len(splited)

        for route in splited:
            print >> stream, " ".join(str(i) for i in route), 0
