
import sys
from math import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a,b,c,d = map(int,input().split())

def lcm(x,y):
    return x*y//gcd(x,y)

def judge(lim, x,y):
    return lim - lim//x - lim//y + lim//lcm(x,y)

ret = judge(b,c,d) - judge(a-1,c,d)

print(ret)