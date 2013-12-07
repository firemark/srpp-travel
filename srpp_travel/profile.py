import config
import cProfile

from models import World, Breeder


def f():
    world = World.from_file("data/100_k=3")
    breeder = Breeder(world)
    for _ in range(config.iterations):
        breeder.do_shit()

cProfile.run("f()", sort='cumulative')
