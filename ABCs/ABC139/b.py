
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

A, B = map(int, input().split())
ans = -(-(B-1)//(A-1))

print(ans)
