"""
Requirements

Passing unit tests
No use of third-party libraries - only built in + - / * operators and the math module
No use of for or while loops
"""


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
    """
    [a b]  + [c d]  = [a+c b+d]

    Matrix + Matrix = Matrix
    """
    if len(x) != len(y):
        raise ShapeException("Shape rule: the vectors must be the same size.")
    else:
        return [x[z] + y[z] for z in range(len(x))]


def vector_sub(x, y):
    """
    [a b]  - [c d]  = [a-c b-d]

    Matrix + Matrix = Matrix
    """
    if len(x) != len(y):
        raise ShapeException("Shape rule: the vectors must be the same size.")
    else:
        return [x[z] - y[z] for z in range(len(x))]


def vector_sum(*args):
    """Can take any number of vectors and add them together."""
    lst = [len(x) for x in args]
    if any(x != lst[0] for x in lst):
        raise ShapeException("Shape rule: the vectors must be the same size.")
    else:
        return [sum(x) for x in zip(*args)]


def dot(x, y):
    """
    dot([a b], [c d])   = a * c + b * d

    dot(Vector, Vector) = Scalar
    """
    if len(x) != len(y):
        raise ShapeException("Shape rule: the vectors must be the same size.")
    else:
        return sum([x[i] * y[i] for i in range(len(x))])
