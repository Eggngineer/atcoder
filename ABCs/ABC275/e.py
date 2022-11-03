
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m,k = map(int,input().split())
dp = [[0]*m*k]*k
dp[0][:m] = [1]*m
for i in range(1,k):
    for j in range(i,i+m*(i+1):
        dp[i][j] = sum(dp[i-1][:j])
