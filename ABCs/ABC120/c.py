
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(map(int, list(input().rstrip())))

ans = 0
red, blue = 0, 1
cred, cblue = 0, 0

for cube in s:
    if cube == red:
        if cblue:
            cblue -= 1
            ans += 2
        else:
            cred += 1
    if cube == blue:
        if cred:
            cred -= 1
            ans += 2
        else:
            cblue += 1

print(ans)
