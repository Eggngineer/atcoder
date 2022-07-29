
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

l1, r1, l2, r2 = map(int, input().split())

ans = 0
if r1 < l2 or r2 < l1:
    ans = 0
else:
    if l1 < l2 and r1 < r2:
        ans = r1-l2
    elif l1 < l2 and r2 <= r1:
        ans = r2-l2
    elif l2 <= l1 and r1 < r2:
        ans = r1-l1
    else:
        ans = r2-l1

print(ans)
