import argparse
from models import World, Breeder
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
        value = breeder.get_winner().value
        scores.append(value)

    winner = breeder.get_winner()
    breeder.print_result()

    # to another function
    import pylab as pl
    #results
    pl.plot(scores)
    pl.title("The best result: %d" % winner.value)
    pl.show()

    #graph

    cities = world.cities["cor"][1:]
    magazine = world.magazine["cor"]
    cors = winner.to_routes_with_magazine()["cor"]

    # http://stackoverflow.com/questions/7519467/
    pl.quiver(
        cors[:-1, 0], cors[:-1, 1],  # X, Y
        cors[1:, 0] - cors[:-1, 0],  # dX
        cors[1:, 1] - cors[:-1, 1],  # dY
        scale_units='xy', angles='xy', scale=1,
        width=0.001, headwidth=10, headlength=10,
        headaxislength=10
    )
    pl.plot(magazine[0], magazine[1], 'go')
    pl.plot(cities[:, 0], cities[:, 1], 'ro')

    pl.show()


if __name__ == "__main__":
    run(get_parser().parse_args())
