
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,k = map(int,input().split())



ansl = []
for i in range(1,n+1):
    tmp = i+k
    if tmp >n:
        tmp = tmp %n
    ansl.append(tmp)

if k > n//2:
    print(-1)
else:
    for i in range(n):
        print(ansl[i],end=" ")
    print()