
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def cost(a,b):
    return abs(a-b)

n = int(input())
h = list(map(int,input().split()))

dp = [0]*n
dp[1] = abs(h[1]-h[0])



for i in range(2,n):
    dp[i] = min(dp[i-2]+cost(h[i],h[i-2]),dp[i-1]+cost(h[i],h[i-1]))

print(dp[~0])
