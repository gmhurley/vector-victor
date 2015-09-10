from math import sqrt


class ShapeException(Exception):
    pass

shape_rule = "The vectors must be the same size."


def shape(inp):
    try:
        y = len(inp[0])
        return (len(inp), y)
    except TypeError:
        return (len(inp), )


def vector_add(x, y):
    if len(x) != len(y):
        raise ShapeException(shape_rule)
    else:
        return [x[z] + y[z] for z in range(len(x))]


def vector_sub(x, y):
    if len(x) != len(y):
        raise ShapeException(shape_rule)
    else:
        return [x[z] - y[z] for z in range(len(x))]


def vector_sum(*args):
    lst = [len(x) for x in args]
    if any(x != lst[0] for x in lst):
        raise ShapeException(shape_rule)
    else:
        return [sum(x) for x in zip(*args)]


def dot(x, y):
    if len(x) != len(y):
        raise ShapeException(shape_rule)
    else:
        return sum([x[i] * y[i] for i in range(len(x))])


def vector_multiply(x, y):
    return [z * y for z in x]


def vector_mean(*args):
    return([v/len([x for x in args]) for v in vector_sum(*[x for x in args])])


def magnitude(v):
    return sqrt(sum([x**2 for x in v]))


def matrix_row(inp, pos):
    return inp[pos]


def matrix_col(inp, pos):
    return [x[pos] for x in inp]


def matrix_scalar_multiply(inp, scalar):
    return [[x * scalar for x in row] for row in inp]


def matrix_vector_multiply(matrix, lst):
    if len(matrix_row(matrix, 0)) != len(lst):
        raise ShapeException("The number of rows of the vector must equal the number of columns of the matrix.")
    else:
        multiplied = [[x[idx] * lst[idx] for idx in range(len(lst))] for x in matrix]
        return [sum(x) for x in multiplied]
