
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)

ans = sum(a[0::2])-sum(a[1::2])

print(ans)
