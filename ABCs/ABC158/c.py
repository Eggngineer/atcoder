
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
v = list(map(int, input().split()))

v = sorted(v)

ans = v[0]/(2**(n-1))

for i in range(1, n):
    w = 1/(2**(n-i))
    ans += v[i]*w

print(ans)
