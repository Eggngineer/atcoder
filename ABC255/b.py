import sys
input = sys.stdin.readline
import math
from pprint import pprint

N, K = map(int,input().rstrip('\n').split())

A = list(map(int, input().rstrip('\n').split()))
for i in range(len(A)):
    A[i]  -= 1

XY = [list(map(float, input().rstrip('\n').split())) for _ in range(N)]

def norm(xy1,xy2):
    return math.sqrt((xy1[0]-xy2[0])**2+(xy1[1]-xy2[1])**2)

nb = []




for i in range(N):
    nb.append([])
    for j in range(N):
        nb[i].append(norm(XY[i],XY[j]))

maxNorm = float(0)

for i in range(N):
    if i in A:
        maxNorm = max(maxNorm, max(nb[i]))

pprint(maxNorm)
