
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


d = defaultdict(int)

n = int(input())
a = list(map(int, input().split()))

for ai in a:
    d[ai] += 1

keys = list(d.keys())


ans = 0
for key in keys:
    x = d[key]+d[key-1]+d[key+1]
    ans = max(ans, x)

print(ans)
