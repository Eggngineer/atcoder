
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

x, y = map(int, input().split())

i = 0

ans = 0
while x*2**i <= y:
    ans += 1
    i += 1

print(ans)
