from numpy import array, diff, hypot, sum, insert


def add_magazine(places, magazine):
    """ add magazine as first element in every vector """
    return insert(places, 0, magazine, axis=1)


def compute_distance(places):
    d = diff(places['cor'], axis=0)
    return sum(hypot(d[:, 0], d[:, 1]))


def compute_distance_with_magazine(places, magazine):
    with_magazine = join_magazine(places, magazine)
    return compute_distance(with_magazine)
