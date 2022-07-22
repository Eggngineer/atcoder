
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int, input().split()))

print(sum(a)-len(a))
