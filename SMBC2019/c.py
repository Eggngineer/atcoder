
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

x = int(input())

if x % 100 > 5*(x//100):
    print(0)
else:
    print(1)
