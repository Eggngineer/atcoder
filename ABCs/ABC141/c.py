
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]
p = dict(zip(list(range(n)), [0]*n))

for _a in a:
    p[_a-1] += 1
v = list(p.values())
vmax = max(v)
for i in range(n):
    if v[i] - q > -k:
        print('Yes')
    else:
        print('No')
