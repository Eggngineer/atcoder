
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
A = list(map(int, input().split()))

ans = 0
r = 0
sum = 0
for l in range(N):
    while r < N and sum ^ A[r] == sum+A[r]:
        sum += A[r]
        r += 1
        ans += r-l
    sum -= A[l]

print(ans)
