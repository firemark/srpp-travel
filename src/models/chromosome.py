class Chromosome(object):
    genes = []
    value = -1.0
    magazine = None
    places_in_row = None

    def __init__(self, genes, magazine, places_in_row):
        self.genes = genes
        self.magazine = magazine
        self.places_in_row = places_in_row
