
import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def score(x: int)->int:
    return x*(x-1)//2

n = int(input())
a = list(map(int,input().split()))

d = defaultdict(int)
for ai in a:
    d[ai]+=1

all_sum = 0
for key in d.keys():
    all_sum += score(d[key])


for ai in a:
    print(all_sum - score(d[ai]) + score(d[ai]-1))