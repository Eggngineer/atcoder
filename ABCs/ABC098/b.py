
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
s = list(input().rstrip())

ans = 0
for i in range(1, n):
    l, r = set(s[:i]), set(s[i:])
    ans = max(len(l & r), ans)

print(ans)
