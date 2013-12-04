from models import Chromosome, Place

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

    def mutatate(self, chromosome):
        random_gene_id_1 = randint(1, len(chromosome.genes) -1)
        random_gene_id_2 = randint(1, len(chromosome.genes) -1)
        
        temporary_gene_1 = chromosome.genes[random_gene_id_1]
        temporary_gene_2 = chromosome.genes[random_gene_id_2]
        chromosome.genes[random_gene_id_1] = temporary_gene_2
        chromosome.genes[random_gene_id_2] = temporary_gene_1

    #TODO repair this shit
    def crossover(self, chromosome1, chromosome2):
        half_length = len(self.genes)/2
        del chromosome1.genes[half_length:]
        for gene in chromosome2.genes[:half_length]:
            chromosome1.genes.append(gene)
        return chromosome1

