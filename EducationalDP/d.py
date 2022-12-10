
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,W = map(int,input().split())
dp = [[0]*(W+1)]*(n+1)

wv = [list(map(int,input().split())) for _ in range(n)]

for i,data in enumerate(wv):
    print(dp)
    w,v = data
    for th in range(W+1):
        if w<=th:
            dp[i+1][th] = max(dp[i][th-w]+v,dp[i][th])
        else:
            dp[i+1][th] = dp[i][th]

print(dp)