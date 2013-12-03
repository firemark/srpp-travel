from place import Place

class Chromosome(object):

    genes = []
    value = -1.0
    magazine = None
    places_in_row = None

    def __init__(self, genes, magazine, places_in_row):
        self.genes = genes
        self.magazine = magazine
        self.places_in_row = places_in_row

    def do_mutation(self):
        random_gene_id_1 = randint(1, len(self.genes))
        random_gene_id_2 = randint(1, len(self.genes))
        
        temporary_gene_1 = self.genes[random_gene_id_1]
        temporary_gene_2 = self.genes[random_gene_id_2]
        self.genes[random_gene_id_1] = temporary_gene_2
        self.genes[random_gene_id_2] = temporary_gene_1

    # TODO: make this method better. This is ugly
    def do_evaluation(self):
        prev_place = self.magazine
        counter = 0
        for place in genes:
            length += place.distance(prev_place)
            prev_place = place
            counter += 1
            
            # return to magazine
            if counter == self.places_in_row :
                prev_place = self.magazine
                length += place.distance(prev_place)
                counter = 0

        self.value = length

    def do_crossover(self, other_chromosome):
        half_length = len(self.genes)/2
        del self.genes[half_length:]
        for gene in other_chromosome.genes[:half_length]
            self.genes.append(gene)
