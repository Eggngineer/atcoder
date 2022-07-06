
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

H, W = map(int, input().split())

print(-(-H*W//2) if H != 1 and W != 1 else 1)
