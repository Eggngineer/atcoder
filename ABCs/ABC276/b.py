
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = list(map(int,input().split()))
d = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

for i in range(1,n+1):
    print(len(d[i]),*sorted(d[i]))