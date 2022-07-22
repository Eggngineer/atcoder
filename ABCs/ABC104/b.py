
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = input().rstrip()

slow = list(s.lower())
s = list(s)

slow[0] = 'A'
for i in range(2, len(s)):
    if s[i] == 'C':
        slow[i] = 'C'
        break

if s == slow and 'C' in s[2:-1]:
    print('AC')
else:
    print('WA')
