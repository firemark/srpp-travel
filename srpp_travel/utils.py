from numpy import diff, hypot, sum, insert, hstack


def add_magazine(routes, magazine):
    """ add magazine as first element in every vector """
    return [insert(route, 0, magazine, axis=0) for route in routes]


def to_matrix_of_cords(routes):
    return hstack(routes)['cor']


def compute_distance(routes):
    #
    d = diff(routes, axis=0)
    return sum(hypot(d[:, 0], d[:, 1]))


def compute_distance_with_magazine(routes, magazine):
    with_magazine = add_magazine(routes, magazine)
    return compute_distance(to_matrix_of_cords(with_magazine))
