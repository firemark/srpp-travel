import argparse
from models import World
import pylab as pl
from numpy import array


def get_parser():
    parser = argparse.ArgumentParser(description='Srpp graph viewer')
    parser.add_argument("cities")
    parser.add_argument("routes")

    return parser


def run(args):
    world = World.from_file(args.cities)
    with open(args.routes) as f:
        routes = f.read().split("\n")[2:]
        data = sum(
            (
                [(x, i) for x in r.split()]
                for i, r in enumerate(routes)
            ), []
        )

    cities = array([place.coordinates for place in world.cities])
    cors = array([cities[int(index)] for index, _ in data])
    colors = array([color for _, color in data])
    magazine = world.magazine.coordinates

    pl.quiver(
        cors[:-1, 0], cors[:-1, 1],  # X, Y
        cors[1:, 0] - cors[:-1, 0],  # dX
        cors[1:, 1] - cors[:-1, 1],  # dY
        colors,
        scale_units='xy', angles='xy', scale=1,
        width=0.002, headwidth=10, headlength=10,
        headaxislength=10
    )
    pl.plot(magazine[0], magazine[1], 'go')
    pl.plot(cities[1:, 0], cities[1:, 1], 'ro')

    pl.show()


if __name__ == "__main__":
    run(get_parser().parse_args())
