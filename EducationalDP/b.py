
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def cost(a,b):
    return abs(a-b)

n,k = map(int,input().split())
h = list(map(int,input().split()))

dp = [1e16]*n
dp[0]=0

for i in range(1,n):
    stt = max(i-k,0)
    for j in range(stt,i):
        dp[i] = min(dp[i], dp[j]+cost(h[i],h[j]))

print(dp[~0])