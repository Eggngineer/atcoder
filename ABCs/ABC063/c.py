
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
s = [int(input()) for _ in range(n)]

sidx = sorted(range(len(s)), key=lambda x:s[x])

result = sum(s)

for idx in sidx:
    if result %10 == 0:
        if s[idx] %10 == 0:
            continue
        else:
            result-=s[idx]
            break
    else:
        break
else:
    result = 0


print(result)