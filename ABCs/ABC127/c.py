
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]

nmax = 10**5+1

area = [0]*nmax
for i in range(m):
    area[lr[i][0]-1] += 1
    area[lr[i][1]] -= 1

for i in range(1, nmax):
    area[i] += area[i-1]

ans = 0
for i in range(0, nmax):
    if area[i] == m:
        ans += 1
print(ans)
