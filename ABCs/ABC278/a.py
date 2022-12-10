
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,k = map(int,input().split())
a = list(map(int,input().split()))


for i in range(k,n+k):
    if i<n:
        print(a[i], end=" ")
    else:
        print(0, end=" ")
print()