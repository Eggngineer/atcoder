
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, k = map(int, input().split())
hs = [int(input()) for _ in range(n)]
hs.sort()

ans = hs[~0]-hs[0]

head = 0
tail = k-1

while tail < n:
    ans = min(ans, hs[tail]-hs[head])
    head += 1
    tail += 1
print(ans)
