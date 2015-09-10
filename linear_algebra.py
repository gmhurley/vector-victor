"""
Requirements

Passing unit tests
No use of third-party libraries - only built in + - / * operators and the math module
No use of for or while loops
"""
from math import sqrt


class ShapeException(Exception):
    pass


def shape(inp):
    """
    Takes a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)
    """
    try:
        y = len(inp[0])
        return (len(inp), y)
    except TypeError:
        return (len(inp), )


def vector_add(x, y):
    if len(x) != len(y):
        raise ShapeException("Shape rule: the vectors must be the same size.")
    else:
        return [x[z] + y[z] for z in range(len(x))]


def vector_sub(x, y):
    if len(x) != len(y):
        raise ShapeException("Shape rule: the vectors must be the same size.")
    else:
        return [x[z] - y[z] for z in range(len(x))]


def vector_sum(*args):
    lst = [len(x) for x in args]
    if any(x != lst[0] for x in lst):
        raise ShapeException("Shape rule: the vectors must be the same size.")
    else:
        return [sum(x) for x in zip(*args)]


def dot(x, y):
    if len(x) != len(y):
        raise ShapeException("Shape rule: the vectors must be the same size.")
    else:
        return sum([x[i] * y[i] for i in range(len(x))])


def vector_multiply(x, y):
    return [z * y for z in x]


def vector_mean(*args):
    return([v/len([x for x in args]) for v in vector_sum(*[x for x in args])])


def magnitude(v):
    return sqrt(sum([x**2 for x in v]))
