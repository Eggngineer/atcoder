
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
drinks = [list(map(int, input().split())) for _ in range(n)]
drinks.sort(key=lambda x: x[0])

ans = 0

for drink in drinks:
    prc, stk = drink

    if m < stk:
        stk = m

    ans += prc*stk
    m -= stk

    if m == 0:
        break

print(ans)
