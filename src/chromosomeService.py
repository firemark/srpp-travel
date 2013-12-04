from models import Chromosome, Place
from random import randint

class ChromosomeService(object):
    
    def evaluate(self, chromosome):
        prev_place = chromosome.magazine
        counter = 0
        length = 0.0
        for place in chromosome.genes:
            length += place.distance(prev_place)
            prev_place = place
            counter += 1
            
            # return to magazine
            if counter == chromosome.places_in_row :
                prev_place = chromosome.magazine
                length += place.distance(prev_place)
                counter = 0

        chromosome.value = length

    def mutate(self, chromosome):
        random_gene_id_1 = randint(1, len(chromosome.genes) -1)
        random_gene_id_2 = randint(1, len(chromosome.genes) -1)
        
        temporary_gene_1 = chromosome.genes[random_gene_id_1]
        temporary_gene_2 = chromosome.genes[random_gene_id_2]
        chromosome.genes[random_gene_id_1] = temporary_gene_2
        chromosome.genes[random_gene_id_2] = temporary_gene_1

    #TODO repair this shit
    def crossover(self, chromosome1, chromosome2):
        # half_length = len(chromosome1.genes)/2
        # del chromosome1.genes[half_length:]
        # for gene in chromosome2.genes[:half_length]:
        #     chromosome1.genes.append(gene)
        # return chromosome1

        print "crossover chromosome"
        # get cutting range
        cut_start = randint(0, len(chromosome1.genes) -2)
        cut_end = randint(cut_start, len(chromosome1.genes) -1)

        child_genes_ugly = []
        child_genes_ugly = chromosome2.genes
        
        # paste fragment of chromosome1 genes
        child_genes_ugly[cut_start:cut_start] = chromosome1.genes[cut_start:cut_end]

        # remove duplicates from child genes. Here be dragons. DO NOT TOUCH IT
        child_genes = []
        [child_genes.append(i) for i in child_genes_ugly if not child_genes.count(i)]

        # create and return child chromosome
        child_chromosome = Chromosome(child_genes, chromosome1.magazine, chromosome1.places_in_row)
        return child_chromosome
