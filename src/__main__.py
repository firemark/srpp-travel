import argparse
from models import World, Result
from breeder import Breeder
from config import iterations


def get_parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("path_to_file", metavar="file", help="path to file")

    return parser


def run(args):
    world = World.from_file(args.path_to_file)

    print("filename: %s" % world.filename)
    print("magazine x: {} y: {}".format(*world.magazine))
    print("len of cities: %d" % len(world.cities))
    print("k: %d" % world.k)

    print("----")

    breeder = Breeder(world)
    for _ in xrange(iterations):
        breeder.do_shit()

    result = Result(breeder.get_best_chromosome())
    result.print_result()


if __name__ == "__main__":
    run(get_parser().parse_args())
