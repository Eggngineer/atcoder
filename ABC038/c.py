
from math import factorial
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


N = int(input())
a = list(map(int, input().split()))

l, r = 0, 0
prev = 0
ans = 0

while l < N:
    tmp = 0
    while r < N and prev < a[r]:
        prev = a[r]
        tmp += 1
        r += 1
    ans += tmp
    if tmp >= 2:
        ans += cmb(tmp, 2)
    prev = 0
    l = r

print(ans)
