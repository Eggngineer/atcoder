
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


d = defaultdict(int)

n = int(input())
for _ in range(n):
    s = input().rstrip()
    d[s] += 1
m = int(input())
for _ in range(m):
    s = input().rstrip()
    d[s] = max(d[s]-1, 0)

print(max(d.values()))
