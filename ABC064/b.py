
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a, b = map(int, input().split())
s = list(input().rstrip())

if s[a] == "-" and len(s)-1 == len(s)-s.count('-'):
    print('Yes')
else:
    print('No')
