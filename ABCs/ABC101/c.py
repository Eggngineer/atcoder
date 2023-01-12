
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n,k = map(int,input().split())
a = list(map(int,input().split()))

ret = -(-(n-1)//(k-1))

print(ret)
