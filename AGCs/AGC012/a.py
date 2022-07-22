
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
ans = 0

for i in range(1, n+1):
    ans += a[2*i-1]

print(ans)
