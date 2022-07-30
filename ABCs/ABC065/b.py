
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

q = defaultdict(bool)

n = int(input())
a = [0] + [int(input()) for _ in range(n)]

i = 1
cnt = 0

for _ in range(n):
    cnt += 1
    if not q[i]:
        if a[i] == 2:
            ans = cnt
            break
        q[i] = True
        i = a[i]
    else:
        ans = -1
        break


print(ans)
