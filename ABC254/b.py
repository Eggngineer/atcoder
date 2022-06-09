import sys
input = sys.stdin.readline
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N = int(input())
for i in range(N):
    for j in range(i+1):
        print(cmb(i,j),end=" ")
    print()