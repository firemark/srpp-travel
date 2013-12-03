from random import shuffle, randint

from chromosome import Chromosome
from models import World
from config import mutation_chance_perc, population

class Breeder(object):

    chromosome_list = None
    chromosome_list_paired = None

    def __init__(self, chromosome_list):
        self.chromosome_list = []
        self.chromosome_list_paired = []

    def mutate_chromosomes(self):
        for chromosome in chromosome_list
            random_percent = randint(1, 100)
            if random_percent <= mutation_chance_perc:
                chromosome.do_mutation()

    def sort_chromosomes_by_value(self):
        for chromosome in self.chromosome_list
            chromosome.do_evaluation()
        self.chromosome_list.sort(key=lambda chromosome: chromosome.value)

    def remove_weak_chromosomes(self):
        sort_chromosome_list_by_value()
        half_length = len(chromosome_list)/2
        del chromosome_list[half_length:]

    def pair_chromosomes(self):
        while(len(chromosome_list) > 1):
            pair = []
            
            random_number1 = randint(0, len(chromosome_list))
            pair[0] = chromosome_list.pop(random_number1)
            random_number2 = randint(0, len(chromosome_list))
            pair[1] = chromosome_list.pop(random_number2)
            
            chromosome_list_paired.append(pair)
        
        # if not even number of chromosomes, pair last chromosome with his clone
        if len(chromosome_list) == 1 :
            pair[0] = chromosome_list[0]
            pair[1] = chromosome_list[0]

    def crossover_chromosomes(self):
        for pair in self.chromosome_list_paired:
            chromosome0 = pair[0].do_crossover(pair[1])
            chromosome1 = pair[1].do_crossover(pair[0])
            self.chromosome_list.append(chromosome0)
            self.chromosome_list.append(chromosome1)

        chromosome_list_paired = []

    def do_shit(self):
        remove_weak_chromosomes()
        pair_chromosomes()
        crossover_chromosomes()
        mutate_chromosomes()

    def get_best_chromosome(self):
        sort_chromosomes_by_value()
        return self.chromosome_list[0]

    def feed_breeder(self, world):
        magazine_place = world.get_magazine_place()
        places_list = world.get_places_list()
        places_in_row = world.k

        for number in range(population)
            shuffle(places_list)
            chromosome = Chromosome(places_list, magazine_place, places_in_row)
            self.chromosome_list.append(chromosome)

