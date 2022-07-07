
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
d = list(map(int, input().split()))

d = sorted(d)

div = n//2
ans = d[div] - d[div-1]

print(ans)
