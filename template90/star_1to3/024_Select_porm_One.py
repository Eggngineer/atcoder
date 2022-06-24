"""
ABC086-C "Traveling"
AGC002-A "Range Product"
AGC020-A "Move and Win"
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, K = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [abs(A[i]-B[i]) for i in range(N)]
C_sum =sum(C)

if K >= C_sum:
    flag = (C_sum -K) % 2
else:
    flag = 1

if flag == 0:
    print("Yes")
else:
    print("No")
