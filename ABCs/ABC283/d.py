
import sys
import re
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input().rstrip())
res = "Yes"
boxes ={}

while s:
    si = s.pop(0)
