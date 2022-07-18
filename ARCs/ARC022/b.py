
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
A = list(map(int, input().split()))

r = 0
ans = 0
prev = -1
tmp = 0
exist = {}
for l in range(N):
    while r < N and A[r] not in exist:
        exist[A[r]] = True
        prev = A[r]
        tmp += 1
        r += 1
    ans = max(ans, tmp)
    del exist[A[l]]
    tmp -= 1
print(ans)
