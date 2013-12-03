from random import shuffle, randint
from breeder import Breeder
from config import iterations
from sys import stdout

def compute_result(world):
    # styk breedera i reszty programu
    breeder = Breeder()
    breeder.feed_breeder(world)

    for number in xrange(iterations):
        breeder.do_shit()

    result_chromosome = breeder.get_best_chromosome()
    
    return result_chromosome

def print_result(result_chromosome, stream=stdout):

    stream.write("WYNIK: %f\n" % result_chromosome.value)
    stream.write("ILOSC GENOW: %d\n" % len(result_chromosome.genes))

    counter = 0
    #stream.write("%d : %d\n" % result_chromosome.magazine[0], result_chromosome.magazine[1])
    print result_chromosome.magazine
    for place in result_chromosome.genes:
        print place
        counter += 1

        if counter == result_chromosome.places_in_row :
            print result_chromosome.magazine
            counter = 0
