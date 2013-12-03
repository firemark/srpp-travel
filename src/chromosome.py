from random import shuffle, randint

class Chromosome(object):

    gens = []

    def __init__(self, gens):
        self.gens = gens

    def do_mutation(self):
        random_gene_id_1 = randint(1, len(self.gens))
        random_gene_id_2 = randint(1, len(self.gens))
        
        temporary_gene_1 = self.gens[random_gene_id_1]
        temporary_gene_2 = self.gens[random_gene_id_2]
        self.gens[random_gene_id_1] = temporary_gene_2
        self.gens[random_gene_id_2] = temporary_gene_1


