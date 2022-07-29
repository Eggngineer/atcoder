
from itertools import permutations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def norm(p1, p2):
    ret = 0
    for i in range(2):
        ret += ((p1[i]-p2[i])**2)
    ret = ret**(1/2)

    return ret


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

dMap = []
for i in range(n):
    line = []
    for j in range(n):
        line.append(norm(xy[i], xy[j]))
    dMap.append(line)

ans = 0
cnt = 0

for rt in permutations(list(range(n))):
    cnt += 1
    for i in range(len(rt)-1):
        ans += dMap[rt[i]][rt[i+1]]

ans /= cnt

print(ans)
