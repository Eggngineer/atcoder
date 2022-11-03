
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input().rstrip())
ans = list('keyence')

result = 'NO'

for i in range(len(s)):
    for j in range(i,len(s)):
        q = s[:i]+s[j:]
        if q == ans:
            result = 'YES'
            break

print(result)