
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input())
acgt = set(['A', 'C', 'G', 'T'])

ans = 0
tmp = 0
for ch in s:

    if ch in acgt:
        tmp += 1
    else:
        tmp = 0
    ans = max(ans, tmp)

print(ans)
