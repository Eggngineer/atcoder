
import sys
from math import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n,x = map(int,input().split())
xi = list(map(int,input().split()))
xi = [0]+[abs(xj-x) for xj in xi]

ret = gcd(xi[0],xi[1])
for i in range(2,n+1):
    ret = gcd(ret,xi[i])

print(ret)