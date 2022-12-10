
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
dp = list(map(int,input().split()))
ndp = [0]*3



for _ in range(n-1):
    sc = list(map(int,input().split()))
    ndp[0] = max(dp[1]+sc[0],dp[2]+sc[0])
    ndp[1] = max(dp[2]+sc[1],dp[0]+sc[1])
    ndp[2] = max(dp[0]+sc[2],dp[1]+sc[2])
    dp[0:] = ndp[0:]

print(max(dp))