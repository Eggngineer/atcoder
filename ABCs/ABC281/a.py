
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

for i in reversed(range(n+1)):
    print(i)