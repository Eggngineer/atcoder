
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a, b, c, k = map(int, input().split())

if k % 2 == 0:
    print(a-b)
else:
    print(b-a)
