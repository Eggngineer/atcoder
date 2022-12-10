
import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,q = map(int,input().split())
tab = [ list(map(int,input().split())) for _ in range(q)]

folist = {}

for i in range(q):
    t,a,b = tab[i]
    if t ==1 :
        if not a in folist:
            folist[a] = defaultdict(int)
        folist[a][b] = 1
    elif t ==2 :
        if not a in folist:
            folist[a] = defaultdict(int)
        folist[a][b] = 0
    else:
        if a in folist and b in folist and b in folist[a] and a in folist[b]:
            if folist[a][b] ==1 and folist[b][a] ==1:
                print("Yes")
            else:
                print("No")
        else:
            print("No")