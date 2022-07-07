
from cmath import cos
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a, b, m = map(int, input().split())
ida = list(range(a))
ref = list(map(int, input().split()))
dref = dict(zip(ida, ref))
idb = list(range(b))
mw = list(map(int, input().split()))
dmw = dict(zip(idb, mw))
cp = [list(map(int, input().split())) for _ in range(m)]

x, y, c = list(range(3))
cmin = min(ref)+min(mw)
for i in range(m):
    cost = dref[cp[i][x]-1] + dmw[cp[i][y]-1] - cp[i][c]
    cmin = min(cmin, cost)

print(cmin)
