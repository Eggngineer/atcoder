import sys
input = sys.stdin.readline

R,C = map(int,input().rstrip('\n').split())

A = [list(map(int, input().rstrip('\n').split())) for _ in range(2)]

print(A[R-1][C-1])
