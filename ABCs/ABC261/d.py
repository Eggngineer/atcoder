
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

inf = 1 << 60

n, m = map(int, input().split())
x = list(map(int, input().split()))

bonus = [0]*(n+1)
for _ in range(m):
    c, y = map(int, input().split())
    bonus[c] = y

dp = [-inf] * (n+1)
dp[0] = 0
for i in range(n):
    print(dp)
    dp0 = -inf
    for j in range(i, -1, -1):
        dp0 = max(dp0, dp[j])
        dp[j+1] = dp[j] + x[i] + bonus[j+1]
    dp[0] = dp0
print(dp)
print(max(dp))
