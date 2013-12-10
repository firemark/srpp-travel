import argparse
from models import World
from breeder import Breeder
from config import iterations
from sys import stdout
from time import time

def get_parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("path_to_file", metavar="file", help="path to file")
    parser.add_argument("--output", default="")

    return parser


def run(args):
    world = World.from_file(args.path_to_file)
    breeder = Breeder(world)

    itr = 0

    t = time()
    try:
        while True:
            for i in xrange(100):
                breeder.do_iteration()
            itr += 100
            print "t: %.2f %s >> iter[%d] = %.2f" % (
                time() - t,
                world.filename,
                itr,
                breeder.get_best_chromosome().value
            )
    except KeyboardInterrupt:
        pass

    st = open(args.output, "w") if args.output  else stdout
    breeder.print_result(world, st)

if __name__ == "__main__":
    run(get_parser().parse_args())
