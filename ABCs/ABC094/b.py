
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, x = map(int, input().split())
a = list(map(int, input().split()))

spot = [0]*(n+1)

for i in range(1, n+1):
    if i in a:
        spot[i] = 1

ans = min(sum(spot[:x]), sum(spot[x:]))

print(ans)
