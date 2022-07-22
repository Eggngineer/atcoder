
from curses.ascii import NAK
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


ans = 0

for i in range(n):
    ans += min(a[i]+a[i+1], b[i])
    b[i] = max(b[i]-a[i], 0)
    a[i+1] = max(a[i+1] - b[i], 0)


print(ans)
