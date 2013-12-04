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

    def crossover(self, chromosome1, chromosome2):

        # get cutting range
        cut_start = randint(0, len(chromosome1.genes) -2)
        cut_end = randint(cut_start, len(chromosome1.genes) -1)

        child_genes_ugly = []
        child_genes_ugly = chromosome2.genes
        
        # paste fragment of chromosome1 genes
        child_genes_ugly[cut_start:cut_start] = chromosome1.genes[cut_start:cut_end]

        child_genes = self.remove_duplicates_from_list(child_genes_ugly)

        # create and return child chromosome
        child_chromosome = Chromosome(child_genes, chromosome1.magazine, chromosome1.places_in_row)
        return child_chromosome

    # HERE BE DRAGONS. FAST AND FAST. DO NOT TOUCH IT
    def remove_duplicates_from_list(self, seq, idfun=None): 
       # order preserving
       if idfun is None:
           def idfun(x): return x
       seen = {}
       result = []
       for item in seq:
           marker = idfun(item)
           # in old Python versions:
           # if seen.has_key(marker)
           # but in new ones:
           if marker in seen: continue
           seen[marker] = 1
           result.append(item)
       return result