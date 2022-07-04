
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

from pprint import pprint

def mhDist(v1,v2,pow):
    return (abs(v1[0]-v2[0]) + abs(v1[1]-v2[1]))/pow

N = int(input())
xyP = [list(map(int, input().split())) for _ in range(N)]

pMat = []
abiMax = 0

for i in range(N):
    colMat = []
    for j in range(N):
        abi = mhDist(xyP[i][:2],xyP[j][:2],xyP[i][2])
        if abi > abiMax: abiMax=abi
        colMat.append(abi)
    pMat.append(colMat)
pprint(pMat)
