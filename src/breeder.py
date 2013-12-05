from random import shuffle, randint
from models import Result, World, Chromosome
from config import mutation_chance_perc, population


class Breeder(object):

    chromosome_list = None
    chromosome_list_paired = None
    chromosome_list_new_generation = None

    def __init__(self, world):
        self.chromosome_list = []
        self.populate_chromosome_list(world)
        self.chromosome_list_paired = []
        self.chromosome_list_new_generation = []

    def mutate_chromosomes(self):
        for chromosome in self.chromosome_list:
            random_percent = randint(1, 100)
            if random_percent <= mutation_chance_perc:
                chromosome.mutate()

    def sort_chromosomes_by_value(self):
        for chromosome in self.chromosome_list:
            self.evaluate(chromosome)

        self.chromosome_list.sort(
            key=lambda chromosome: chromosome.value, reverse=True)

    def remove_weak_chromosomes(self):
        self.sort_chromosomes_by_value()
        half_length = len(self.chromosome_list) / 2
        del self.chromosome_list[:half_length]

    def pair_chromosomes(self):
        chromosome_list_tmp = []
        chromosome_list_tmp = self.chromosome_list
        while(len(chromosome_list_tmp) > 1):
            pair = []
            random_number1 = randint(0, len(chromosome_list_tmp) - 1)
            pair.append(chromosome_list_tmp.pop(random_number1))
            random_number2 = randint(0, len(chromosome_list_tmp) - 1)
            pair.append(chromosome_list_tmp.pop(random_number2))

            self.chromosome_list_paired.append(pair)

        # if not even number of chromosomes, pair last chromosome with his
        # clone
        if len(chromosome_list_tmp) == 1:
            pair = []
            pair.append(chromosome_list_tmp[0])
            pair.append(chromosome_list_tmp[0])
            self.chromosome_list_paired.append(pair)

    def crossover_chromosomes(self):
        self.pair_chromosomes()
        for chr_A, chr_B in self.chromosome_list_paired:
            self.chromosome_list_new_generation += [
                chr_A.crossover(chr_B),
                chr_B.crossover(chr_A)
            ]

    def overwrite_old_generation_with_new(self):
        self.chromosome_list = self.chromosome_list_new_generation
        self.chromosome_list_new_generation = []
        self.chromosome_list_paired = []

    def do_shit(self):
        self.remove_weak_chromosomes()
        # crossover needs to be done two times
        self.crossover_chromosomes()
        self.crossover_chromosomes()
        self.overwrite_old_generation_with_new()
        self.mutate_chromosomes()

    def get_best_chromosome(self):
        self.sort_chromosomes_by_value()
        return self.chromosome_list[-1]

    def populate_chromosome_list(self, world):
        magazine_place = world.get_magazine()
        places_list = world.get_places_list()
        places_in_row = world.k

        for number in range(population):
            shuffle(places_list)
            chromosome = Chromosome(places_list, magazine_place, places_in_row)
            self.chromosome_list.append(chromosome)

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
