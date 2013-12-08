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
    scores = []

    for number in xrange(iterations):
        breeder.do_shit()
        scores.append(breeder.get_best_chromosome().value)

    breeder.print_result(world)

    from os import system

    gnuplot = """echo "plot \\"-\\" with lines\n{}" | gnuplot -p """
    system(gnuplot.format("\n".join(str(i) for i in scores)))

    try:
        import pylab as pl
    except ImportError:
        exit()
    # results
    winner = breeder.get_best_chromosome()
    pl.plot(scores)
    pl.title("The best result: %d" % winner.value)
    pl.show()

    # graph

    #cities = world.cities["cor"][1:]
    #magazine = world.magazine["cor"]
    #cors = winner.to_routes_with_magazine()["cor"]


if __name__ == "__main__":
    run(get_parser().parse_args())
