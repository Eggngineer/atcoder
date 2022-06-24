"""
ABC162-C "Sum of GCD of Tupples(Easy)"
ABC118-C "Monsters Battle Royal"
ABC125-C "GCD on BlackBoard"
"""


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from math import gcd
from functools import reduce

A,B,C = map(int,input().split())

div = reduce(gcd,(A,B,C))
ans = 0
for x in (A,B,C):
    ans += -(-x//div)
ans -= len((A,B,C))
print(ans)

# from math import gcd
# from functools import reduce
 
# a,b,c = [int(buf) for buf in input().split(" ")]
# gcd_num = reduce(gcd,(a,b,c))
# print(sum((a,b,c)) // gcd_num - len((a,b,c)))