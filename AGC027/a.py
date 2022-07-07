
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, x = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)
ans = 0
for i in range(n):
    if x-a[i] < 0:
        ans = i
        break
    else:
        x -= a[i]
else:
    if x == 0:
        ans = n
    else:
        ans = n-1
print(ans)
