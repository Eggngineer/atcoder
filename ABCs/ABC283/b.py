
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int,input().split()))
ad = dict(zip(range(1,n+1),a))
q = int(input())

for _ in range(q):
    que = list(map(int,input().split()))
    if que[0] == 1:
        ad[que[1]] = que[2]
    else:
        print(ad[que[1]])
