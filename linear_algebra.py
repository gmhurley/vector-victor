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
