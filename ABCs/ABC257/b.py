
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, K, Q = map(int,input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

TAIL = N

for op in L:
    # print(A)
    op -= 1
    if  A[op] < TAIL and A[op]+1 not in A:
        A[op] += 1
    if TAIL in A:
        TAIL -= 1

for i in range(len(A)):
    print(A[i], end="")
    if i != len(A)-1:
        print(" ", end="")
