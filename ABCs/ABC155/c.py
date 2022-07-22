
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


d = defaultdict(int)

n = int(input())
for _ in range(n):
    s = input().rstrip()
    d[s] += 1

freqmax = max(d.values())

ans = []
for key in d.keys():
    if d[key] == freqmax:
        ans.append(key)

ans.sort()

for a in ans:
    print(a)
