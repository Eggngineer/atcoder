
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

w = list(input().rstrip())
d = {}

for al in w:
    if al not in d:
        d[al] = 1
    else:
        d[al] += 1

for v in d.values():
    if v % 2 != 0:
        print('No')
        break
else:
    print('Yes')
