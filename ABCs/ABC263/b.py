
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

d = defaultdict(int)
n = int(input())
p = [0, 0]+list(map(int, input().split()))

i = 2
for person in p[2:]:
    d[i] = person
    i += 1

s = n
cnt = 0
while d[s] != 0:
    s = d[s]
    cnt += 1
print(cnt)
