
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

d, n = map(int, input().split())

if n == 100:
    n += 1

ans = 100**d*n

print(ans)
