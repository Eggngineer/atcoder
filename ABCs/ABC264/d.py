
from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dic = dict(zip(list('atcoder'), list(range(7))))

g = list(range(7))
s = list(input().rstrip())
for i in range(7):
    s[i] = dic[s[i]]


cnt = 0
for i in range(7):
    if s[i] != i:
        tid = s.index(i)
        s = s[:i]+[s[tid]]+s[i:tid]+s[tid+1:]
        cnt += tid-i

print(cnt)
