
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def manhattan(v1: list, v2: list):
    return abs(v1[0]-v2[0])+abs(v1[1]-v2[1])


n,m = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
cd = [list(map(int,input().split())) for _ in range(m)]

results = [0]*n

for i in range(n):
    mh_min = 4e+8
    aibi = ab[i]
    for j  in range(m):
        cjdj = cd[j]
        mh_dist = manhattan(v1=aibi,v2=cjdj)
        if mh_min > mh_dist:
            results[i] = j+1
            mh_min = mh_dist

for result in results:
    print(result)

