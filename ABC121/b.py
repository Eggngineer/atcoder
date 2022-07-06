
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, C = map(int, input().split())
C = -C
B = list(map(int, input().split()))

ans = 0
for _ in range(N):
    f = 0
    A = list(map(int, input().split()))
    for i in range(M):
        f += A[i]*B[i]
    if f > C:
        ans += 1

print(ans)
