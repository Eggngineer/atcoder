"""
AOJ ALDS-1-4-B
ABC077-C Snuke Festival
"""
import sys
input = sys.stdin.readline
from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()

for b in B:
    idx = bisect_left(A,b)
    print(min(abs(A[min(idx, N - 1)] - b), abs(A[max(idx - 1, 0)] - b)))
