
from functools import reduce
from operator import mul
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]

l, r = 0, 0
patterns = []
while l < N:
    had = {}
    while r < N and A[r] not in had:
        had[A[r]] = True
        r += 1
    tmp = r-l
    if r-l >= 2:
        tmp += cmb(r-l, 2)
    patterns.append(tmp)
    l = r

print(patterns[-1])
