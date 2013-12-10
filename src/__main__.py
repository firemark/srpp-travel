import argparse
from models import World
from breeder import Breeder
from config import iterations


def get_parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("path_to_file", metavar="file", help="path to file")

    return parser


def run(args):
    world = World.from_file(args.path_to_file)
    breeder = Breeder(world)

    for number in xrange(iterations):
        breeder.do_shit()

    breeder.print_result(world)

if __name__ == "__main__":
    run(get_parser().parse_args())
