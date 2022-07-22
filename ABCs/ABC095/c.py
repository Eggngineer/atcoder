
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

price = list(map(int, input().split()))
abc, xy = price[:3], price[3:]

ans = 0

a, b, c = abc
x, y = xy

minxy = min(x, y)
if a+b > c*2:
    ans += c*2*minxy
    x, y = x-minxy, y-minxy
if c*2 <= a:
    ans += c*2*max(x, 0)
else:
    ans += a*max(x, 0)
if c*2 <= b:
    ans += c*2*max(y, 0)
else:
    ans += b*max(y, 0)

print(ans)
