
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,k = map(int,input().split())
p = list(map(int,input().split()))


def tsum(n: int = 6) -> float:
    return float(n*(n+1)/2) if n > 0 else 0

e = [0]*n
for i in range(n):
    e[i] = tsum(p[i])/p[i]

ans = 0
for i in range(k):
    ans += e[i]

win_total = ans
for i in range(k,n):
    win_total = win_total + e[i] - e[i-k]
    if win_total>= ans:
        ans = win_total

print("{:.6f}".format(ans))