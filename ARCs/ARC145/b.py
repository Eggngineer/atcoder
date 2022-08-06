
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, a, b = map(int, input().split())
ans = 0


la = n//a
if n >= a:
    if la > 0:
        ans = (la-1)*min(a, b)
    ans += min(n % a+1, b)
else:
    ans = 0

print(ans)
