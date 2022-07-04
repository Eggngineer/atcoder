
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, Q = map(int, input().split())
A = list(input().rstrip())
Idx = list(range(N))

D = dict(zip(Idx, A))

pushes = 0

for _ in range(Q):
    op, num = map(int, input().split())
    if op == 1:
        pushes -= num
    if op == 2:
        print(D[(num-1+pushes) % N])
