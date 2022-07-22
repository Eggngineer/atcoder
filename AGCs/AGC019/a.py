
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

q, h, s, d = map(int, input().rstrip().split())
n = int(input())

lit1 = min(q*4, h*2, s)
lit2 = d

ans = 0

if lit1*2 < lit2:
    ans += (n // 2) * lit1 * 2
else:
    ans += (n // 2) * lit2

n %= 2

if n:
    ans += lit1

print(int(ans))
