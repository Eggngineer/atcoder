
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
print(n*2**n % 998244353)
