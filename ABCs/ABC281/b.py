
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input().rstrip())
nms = list(map(str,range(10)))
stt, end = s[0],s[~0]
mid = 0

ans = "Yes"

if stt.isupper() and end.isupper() and len(s) >= 8:
    for i in s[1:7]:
        if i not in nms:
            ans="No"
            break
    if s[1] == str(0):
        ans = "No"
else:
    ans = "No"

print(ans)