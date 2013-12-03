from random import shuffle, randint
from models import Result
from breeder import Breeder
from config import iterations

def find_routes(world):
    # styk breedera i reszty programu
    breeder = Breeder()
    breeder.feed_breeder(world)

    for number in range(iterations)
        breeder.do_shit()

    result_world = breeder.get_result_world()
    result = Result(result_world)
    result.length = breeder.get_result_value()
    
    return result
