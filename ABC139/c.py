
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
h = list(map(int, input().split()))

prev = -1
tmp = -1
ans = 0
for p in h:
    if prev < p:
        tmp = 0
    else:
        tmp += 1
    prev = p
    ans = max(ans, tmp)

print(ans)
