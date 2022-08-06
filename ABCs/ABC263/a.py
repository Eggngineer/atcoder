
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

p = list(map(int, input().split()))
d = defaultdict(int)

for c in p:
    d[c] += 1

if 2 in list(d.values()) and 3 in list(d.values()):
    print('Yes')
else:
    print('No')
