
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,k,d = map(int,input().split())
a = list(map(int,input().split()))
b = [a[i]%d for i in range(n)]
dp = [[0 for _ in range(100*100+1)] for _ in range(n+1)]
for i in range(100*100 + 1):
    dp[0][i] = 0

for i in range(n):
    for w in range(100*100+1):
        if w % d == 0:
            if b[i] <= w:
                dp[i+1][w] = max(dp[i][w-b[i]]+a[i],dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]

print(dp[n])