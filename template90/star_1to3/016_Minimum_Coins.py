"""
ABC051-B "Sum of Three Integers"
ABC085-C "Otoshidama"
ABC095-C "Half and Half"
ABC112-C "Pyramid"
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
A,B,C = map(int,input().split())
Limit = 10000
z = Limit

minL = 10000

for x in range(Limit):
    for y in range(Limit):
        if N-A*x-B*y < 0:break
        mod = (N-A*x-B*y)%C
        # print(x,y)
        if mod ==0:
            z = int((N-A*x-B*y)/C)
            minL = min(x+y+z,minL)

print(minL)
