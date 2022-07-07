
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
d, x = map(int, input().split())
ans = 0
for _ in range(n):
    a = int(input())
    ans += -(-d//a)
ans += x
print(ans)
