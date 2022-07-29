from operator import mul
from functools import reduce


def cmb(n, r):
    """
    nCr: Combination 
        n!
    --------
    (n-r)!r!
    """
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def perm(n, r):
    """
    nPr: Permutation
    n!/(n-r)!
    """
    if r == 0:
        return 1
    ret = reduce(mul, range(n, n-r, -1))
    return ret


def fact(n):
    """
    n!: Factorial
    """
    if n == 0:
        return 1
    ret = reduce(mul, range(n, 0, -1))
    return ret
