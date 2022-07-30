
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


d = defaultdict(int)

pro = 0

n = int(input())
a = list(map(int, input().split()))

for p in a:
    rate = p//400
    if rate > 7:
        pro += 1
    else:
        d[rate] += 1


amin = max(len(list(d.keys())), 1)
amax = len(list(d.keys()))+pro
print(amin, amax)
