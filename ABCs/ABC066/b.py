
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = input().rstrip()
l = len(s)

ans = ""
for i in range(l//2):
    p = s[:i+1]
    if p+p in s[:l-1]:
        ans = p+p

print(len(ans))
