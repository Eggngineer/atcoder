
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, k = map(int, input().split())
ans = min(n % k, k-n % k)
print(ans)
