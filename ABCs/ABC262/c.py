
from functools import reduce
from operator import mul
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


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


n = int(input())
a = [0]+list(map(int, input().split()))

eq = 0
pr = 0

for i, q in enumerate(a[1:]):
    if i+1 == q:
        eq += 1
    if a[q] == i+1 and i+1 != q:
        pr += 1

ans = pr//2
if eq >= 2:
    ans += cmb(eq, 2)

print(ans)
