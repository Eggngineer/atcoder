
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

h = int(input())
ans = 0
i = 0

while 2**i <= h:
    ans += 2**i
    i += 1

print(ans)
