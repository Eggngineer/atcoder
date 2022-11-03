
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

anc = {}
n = int(input())
a = list(map(int,input().split()))

for i, parent in enumerate(a):
    idx=i+1
    if idx == 1:
        anc[idx]=0

    anc[2*idx]=anc[parent]+1
    anc[2*idx+1]=anc[parent]+1

for mago in range(1,2*n+1+1):
    print(anc[mago])