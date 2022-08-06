
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
g = [[0]*n for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u-1][v-1] = 1
    g[v-1][u-1] = 1

ans = 0

for i in range(n):
    for j in range(i+1, n):
        if g[i][j] == 1:

            for k in range(j+1, n):
                if g[j][k] == 1 and g[k][i] == 1:
                    ans += 1

print(ans)
