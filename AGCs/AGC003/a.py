
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

move = list(input().rstrip())

n = move.count('N')
s = move.count('S')
w = move.count('W')
e = move.count('E')

if n and s and not w and not e:
    print('Yes')
elif not n and not s and w and e:
    print('Yes')
elif n and s and w and e:
    print('Yes')
else:
    print('No')
