
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

a1r = sum(a1)
a2r = sum(a2)
a1l = 0

ans = 0

for i in range(n):
    a1l += a1[i]
    a1r -= a1[i]
    ans = max(ans, a1l+a2r)
    a2r -= a2[i]

print(ans)
