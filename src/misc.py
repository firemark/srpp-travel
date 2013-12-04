from math import sqrt


def distance(a, b):
    return sqrt(sum((ea - eb) ** 2 for ea, eb in zip(a, b)))
