import argparse
from models import World, Result, Breeder
from config import iterations


def get_parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("path_to_file", metavar="file", help="path to file")

    return parser


def run(args):
    world = World.from_file(args.path_to_file)

    breeder = Breeder(world)
    scores = []
    for _ in xrange(iterations):
        breeder.do_shit()
        scores.append(breeder.get_winner().value)

    winner = breeder.get_winner()
    result = Result(winner.to_routes(), winner.magazine)

    import pylab as pl
    pl.plot(scores)
    pl.show()

    result.print_result()


if __name__ == "__main__":
    run(get_parser().parse_args())
