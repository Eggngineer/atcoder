
from itertools import permutations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

a, b = 0, 0
idx = list(permutations(list(range(1, n+1))))

for i in range(len(idx)):
    if idx[i] == p:
        a = i
    if idx[i] == q:
        b = i

ans = abs(a-b)
print(ans)
