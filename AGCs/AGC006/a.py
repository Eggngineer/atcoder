
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
s = list(input().rstrip())
t = list(input().rstrip())

ans = 0
i, j = 0, 0

while i < n:
    if s[i] != t[j]:
        j = 0
        ans = 0
    if s[i] == t[j]:
        j += 1
        ans += 1
    i += 1

ans = 2 * n - ans
print(ans)