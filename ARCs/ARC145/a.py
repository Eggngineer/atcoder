
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
s = list(input().rstrip())

mid = -(-n//2)

if s[:mid] == s[-mid:].reverse:
    print('Yes')
else:
    if s[0] == s[~0]:
        print('Yes')
    elif s[~0] == 'A' and len(s) > 2:
        print('Yes')
    else:
        print('No')
