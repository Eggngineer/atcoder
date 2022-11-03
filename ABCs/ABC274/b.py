
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

d = {".":0,"#":1}
h,w = map(int,input().split())
x=[0]*w
for _ in range(h):
    col = list(input().rstrip())
    for i in range(w):
        x[i]+=d[col[i]]

print(*x)