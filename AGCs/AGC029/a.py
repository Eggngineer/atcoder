
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input().rstrip())
b, w = 0, 0

ans = 0
for c in s:
    if c == 'B':
        b += 1
    else:
        ans += b

print(ans)
