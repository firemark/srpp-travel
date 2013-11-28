from random import shuffle, randint
from models import Result, Chromosome


def find_routes(world):
    """dummy function"""
    result = Result(world)

    len_cities = len(world.cities)
    cities = range(1, len_cities)
    shuffle(cities)

    temp = 0
    while(temp < len_cities - 1):
        r = randint(1, world.k)
        result.add_route_with_magazine(cities[temp:temp + r])
        temp += r

    return result


def crossover(a, b):
    return Chromosome([])
