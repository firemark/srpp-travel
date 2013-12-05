from models import Chromosome, Place
from utils import compute_distance_with_magazine



class ChromosomeService(object):

    def crossover(self, chromosome1, chromosome2):

        # get cutting range
        cut_start = randint(0, len(chromosome1.genes) - 2)
        cut_end = randint(cut_start, len(chromosome1.genes) - 1)

        child_genes_ugly = []
        child_genes_ugly = chromosome2.genes

        # paste fragment of chromosome1 genes
        child_genes_ugly[cut_start:cut_start] = chromosome1.genes[
            cut_start:cut_end]

        child_genes = self.remove_duplicates_from_list(child_genes_ugly)

        # create and return child chromosome
        child_chromosome = Chromosome(
            child_genes, chromosome1.magazine, chromosome1.places_in_row)
        return child_chromosome

    # HERE BE DRAGONS. FAST AND FAST. DO NOT TOUCH IT
    def remove_duplicates_from_list(self, seq, idfun=None):
        # order preserving
        if idfun is None:
            def idfun(x):
                return x
        seen = {}
        result = []
        for item in seq:
            marker = idfun(item)
            # in old Python versions:
            # if seen.has_key(marker)
            # but in new ones:
            if marker in seen:
                continue
            seen[marker] = 1
            result.append(item)
        return result
