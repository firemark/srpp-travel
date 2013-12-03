import argparse
from models import World
from chromosome import Chromosome
from genetic import compute_result, print_result


def get_parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("path_to_file", metavar="file", help="path to file")

    return parser


def run(args):
    world = World.from_file(args.path_to_file)

    print("filename: %s" % world.filename)
    print("magazine x: %d y: %d" % world.magazine)
    print("len of cities: %d" % len(world.cities))
    print("k: %d" % world.k)

    print("----")

    result = compute_result(world)
    print_result(result)

if __name__ == "__main__":
    run(get_parser().parse_args())
