
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())

if n == 1 or m ==1:
    if n*m ==1:
        print(1)
    else:
        print(n*m - 2)
else:
    print(n*m - 2*n - 2*m + 4)