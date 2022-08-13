
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

r, c = map(int, input().split())

if r > 8:
    r = 15-r+1
if c > 8:
    c = 15-c+1

if r > c:
    r, c = c, r

print('black' if r % 2 == 1 else'white')
