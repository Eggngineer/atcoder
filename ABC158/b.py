
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, a, b = map(int, input().split())
tmp = a+b
ans = n//tmp*a + min(a, n % tmp)

print(ans)
