import sys
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int, input().split()))

odd, even = [0]*2
for num in a:
    if num % 2:
        odd += 1
    else:
        even += 1

ans = 0
ans = 3**n
ans -= 2**even
print(ans)
