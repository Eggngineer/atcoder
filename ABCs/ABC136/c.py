
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
h = list(map(int, input().split()))

ans = None
allowed = h[0]
for cell in h[1:]:
    if cell > allowed:
        allowed = cell-1
    elif cell < allowed:
        ans = 'No'
        break
else:
    ans = 'Yes'

print(ans)
