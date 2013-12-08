import argparse
from models import World, Breeder
from config import iterations


def get_parser():
    parser = argparse.ArgumentParser(description='Srpp travelman')
    parser.add_argument("path_to_file", metavar="file", help="path to file")
    parser.add_argument("--output", help="output format", action='store_true')

    return parser


def run(args):
    world = World.from_file(args.path_to_file)

    breeder = Breeder(world)
    winner = None
    scores = []

    verbose = not args.output

    try:
        if verbose:
            print("iteration best")

        for i in xrange(iterations // 100):
            for _ in xrange(100):
                breeder.do_shit()
                value = breeder.get_winner().value

                if not winner or winner.value > value:
                    winner = breeder.get_winner()

                scores.append(value)

            if verbose:
                print("{:<9} {:.4f}".format((i + 1) * 100, winner.value))

    except KeyboardInterrupt:
        if verbose:
            print("STOP!")

    if args.output:
        winner.print_result()
    else:
        # to another function
        import pylab as pl
        # results
        pl.plot(scores)
        pl.title("The best result: %d" % winner.value)
        pl.show()

        # graph

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
