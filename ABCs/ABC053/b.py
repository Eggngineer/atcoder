
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input().rstrip())

ai, zi = 0, len(s)-1

for i in range(len(s)):
    if s[i] == 'A':
        ai = i
        break

for i in reversed(range(len(s))):
    if s[i] == 'Z':
        zi = i
        break

ans = max(zi-ai + 1, 0)
print(ans)
