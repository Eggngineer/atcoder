
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input().rstrip())
if sorted(s) == sorted(list(set(s))):
    print('yes')
else:
    print('no')
