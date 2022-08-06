
from itertools import combinations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n, m = map(int, input().split())
base = [0]+list(range(1, n+1))
goal = [0]+list(range(m-n+1, m+1))

for cmb in combinations(range(1, m+1), n):
    if cmb > tuple(range(m-n+1, m+1)):
        break
    print(*cmb)
