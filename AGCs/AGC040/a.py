
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


s = list(input().rstrip())
l = [0]*(len(s)+1)

for i in range(len(s)):
    if s[i] == "<":
        l[i+1] = max(l[i]+1, l[i+1])
for i in range(len(s)-1, -1, -1):
    if s[i] == ">":
        l[i] = max(l[i+1]+1, l[i])

print(sum(l))
