
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
h = list(map(int,input().split()))

ans = h[0]
for i in range(n-1):
    ans += max(h[i+1]-h[i],0)

print(ans)