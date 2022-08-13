
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

l, r = map(int, input().split())

ans = " atcoder"

print(ans[l:r+1])
