
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

h,w = map(int,input().split())
a = []
for _ in range(h):
    a+= list(input().rstrip())

row = []
for i in range(h):
    query = a[i*w:i*w+w]
    if query != ["."]*w:
        row.append(i)

col = []
for j in range(w):
    query = a[j::w]
    if query != ["."]*h:
        col.append(j)

for i in row:
    for j in col:
        print(a[i*w+j],end="")
    print()
