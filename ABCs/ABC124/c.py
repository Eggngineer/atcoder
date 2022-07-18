
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input().rstrip())
s = list(map(int, s))

ans1 = 0
for i in range(len(s)):
    k = int(0.5+0.5*(-1)**i)
    ans1 += k ^ s[i]

ans2 = 0
for i in range(1, len(s)+1):
    k = int(0.5+0.5*(-1)**i)
    ans2 += k ^ s[i-1]

print(min(ans1, ans2))
