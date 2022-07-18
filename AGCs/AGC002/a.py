
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a, b = map(int, input().split())

if a*b <= 0:
    print('Zero')
else:
    if a > 0 or (b+1-a) % 2 == 0:
        print('Positive')
    else:
        print('Negative')
