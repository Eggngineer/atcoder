
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

y = int(input())
ans = y

if y % 4 == 0:
    ans += 2
elif y % 4 == 1:
    ans += 1
elif y % 4 == 2:
    ans += 0
else:
    ans += 3


print(ans)
