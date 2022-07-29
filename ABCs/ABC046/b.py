
from functools import reduce
from operator import mul
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def perm(n, r):
    """
    nPr: Permutation
    n!/(n-r)!
    """
    if r == 0:
        return 1
    ret = reduce(mul, range(n, n-r, -1))
    return ret


n, k = map(int, input().split())
ans = k*(k-1)**(n-1)

print(ans)
