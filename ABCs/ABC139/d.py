
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

ans = (n)*(n-1)//2

print(ans)
