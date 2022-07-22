
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = input().rstrip()
t = input().rstrip()

if not set(s) == set(t):
    print('No')
else:
    for i in range(len(s)):
        if s[:i+1] == t[~i:] and s[i+1:] == t[:~i]:
            print('Yes')
            break
    else:
        print('No')
