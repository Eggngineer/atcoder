
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a,b,c,d,e,f = map(int,input().split())

print((a*b*c-d*e*f)%998244353)