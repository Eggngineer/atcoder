"""
ABC091-C "2D Plane 2N Points"
ABC131-D "Megalomania"
CODE FESTIVAL 2016 Grand Final A "1D Matching"  
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(),B.sort()

sum = 0
for i in range(N):
    sum+=abs(A[i]-B[i])
print(sum)
