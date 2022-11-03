
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a,b = map(int,input().split())
print("{:.3f}".format(b/a) )