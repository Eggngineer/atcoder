
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int,input().split()))
q = int(input())

a = dict(zip(range(1,n+1),a))
stock = 0
is_override = 0
or_num = 0

for _ in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        _, x = query
        is_override = 1
        or_num = x
    elif query[0] == 2:
        _, i, x = query
        a[i] += x
    else:
        _, i = query
        print(a[i]*(1-is_override) + or_num * is_override)
