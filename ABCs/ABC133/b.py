
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dist(x, y):
    ans = 0
    for (xi, yi) in zip(x, y):
        ans += (xi-yi)**2
    return ans**(1/2)


n, d = map(int, input().split())

xs = []

ans = 0

for _ in range(n):
    x = list(map(int, input().split()))
    for q in xs:
        d = dist(x, q)
        if d//1 == d:
            ans += 1
    xs.append(x)

print(ans)
