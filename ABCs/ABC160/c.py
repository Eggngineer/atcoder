
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

k, n = map(int, input().split())
a = list(map(int, input().split()))

ans = a[-1]-a[0]
for i in range(1, n):
    ans = min(ans, k-a[i]+a[i-1])
print(ans)
