
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input().rstrip())
if 'a' in s:
    print(len(s)-s[::-1].index('a'))
else:
    print(-1)