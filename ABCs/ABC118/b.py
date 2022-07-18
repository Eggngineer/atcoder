
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
surbey = dict(zip(list(range(m)), [n]*m))

for _ in range(n):
    prefer = list(map(int, input().split()[1:]))
    for p in prefer:
        surbey[p-1] -= 1

zeros = surbey.values()

ans = 0
for zero in zeros:
    if not zero:
        ans += 1

print(ans)
