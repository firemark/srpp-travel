from random import shuffle, randint

from chromosomeService import ChromosomeService
from models import Result, World, Chromosome, Place
from config import mutation_chance_perc, population

class Breeder(object):

    chromosome_list = None
    chromosome_list_paired = None
    chromosomeService = None

    def __init__(self):
        self.chromosome_list = []
        self.chromosome_list_paired = []
        chromosomeService = ChromosomeService()

    def mutate_chromosomes(self):
        for chromosome in self.chromosome_list:
            random_percent = randint(1, 100)
            if random_percent <= mutation_chance_perc:
                chromosomeService.mutate(chromosome)

    def sort_chromosomes_by_value(self):
        for chromosome in self.chromosome_list:
            chromosomeService.evaluate(chromosome)
        
        self.chromosome_list.sort(key=lambda chromosome: chromosome.value)

    def remove_weak_chromosomes(self):
        self.sort_chromosomes_by_value()
        half_length = len(self.chromosome_list)/2
        del self.chromosome_list[half_length:]

    def pair_chromosomes(self):
        while(len(self.chromosome_list) > 1):
            pair = []
            random_number1 = randint(0, len(self.chromosome_list) - 1)
            pair.append(self.chromosome_list.pop(random_number1))
            random_number2 = randint(0, len(self.chromosome_list) - 1)
            pair.append(self.chromosome_list.pop(random_number2))
            
            self.chromosome_list_paired.append(pair)
        
        # if not even number of chromosomes, pair last chromosome with his clone
        if len(self.chromosome_list) == 1 :
            pair = []
            pair.append(self.chromosome_list[0])
            pair.append(self.chromosome_list[0])
            self.chromosome_list_paired.append(pair)

    def crossover_chromosomes(self):
        self.pair_chromosomes()
        for pair in self.chromosome_list_paired:
            chromosome0 = pair[0].do_crossover(pair[1])
            chromosome1 = pair[1].do_crossover(pair[0])
            self.chromosome_list.append(chromosome0)
            self.chromosome_list.append(chromosome1)

        self.chromosome_list_paired = []

    def do_shit(self):
        self.remove_weak_chromosomes()
        self.crossover_chromosomes()
        self.mutate_chromosomes()

    def get_best_chromosome(self):
        self.sort_chromosomes_by_value()
        return self.chromosome_list[0]

    def populate_breeder(self, world):
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
        world.set_magazine = chromosome.magazine
        world.cities[1:] = chromosome.genes[]
        result = Result(world)
        
        return result
