import doctest
def function(a, b):
    """
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> function(2, 3)
    5
    """
    return a + b
doctest.testmod()