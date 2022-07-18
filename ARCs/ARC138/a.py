from operator import truediv
import re

from numpy import amin


N, K = map(int, input().split())
A = list(map(int, input().split()))

s = 0
isOK = False

A_min = 1e9

B=[]
B_sort=[]
B_max = 0

C=[]
C_min = 1e9

def search_minTry(x):
    res = 1
    for y in B_sort:
        if y>x
        res += B.index(y)
    return x


for i in range(K):
    s+=A[i]
    C.append(A[i])
    A_min = min (A_min, A[i])

for j in range(K,N):
    B.append(A[j])
    B_sort.append(A[j])
    B_max = max(B_max,A[j])

B_sort.sort(reverse=True)

if A_min < B_max: isOK = True
res = 0

for x in reversed(C):
    if x < C_min:
        C_min = x
        if x > B_max: 
            pass
        else:
            res = search_minTry(x)
            break