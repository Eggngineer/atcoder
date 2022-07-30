
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

inf = 1 << 60

n, m = map(int, input().split())
x = [0]+list(map(int, input().split()))

b = [0] * (n+1)
for _ in range(m):
    c, y = map(int, input().split())
    b[c] = y

dp = [[-inf]*(n+1) for _ in range(n+1)]
dp[0][0] = 0
pmax = 0
for i in range(1, n+1):
    dp[i][0] = pmax
    for j in range(1, i+1):
        dp[i][j] = dp[i-1][j-1] + x[i] + b[j]
        pmax = max(pmax, dp[i][j])


print(max(dp[n]))
