
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = sorted(list(input().rstrip()))
t = sorted(list(input().rstrip()),reverse=True)

ns,nt = len(s),len(t)

ans = "Yes"
for i in range(min(ns,nt)):
    if s[i] == t[i]:
        continue
    elif s[i] > t[i]:
        ans = "No"
        break
    else:
        break
else:
    if ns >= nt:
        ans = "No"

print(ans)
