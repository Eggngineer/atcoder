
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

x = int(input())

ans = 0
for i in range(1, int(x**(1/2)+1)):
    p = 2
    while i**(p+1) <= x:
        p += 1
        if i == 1:
            break
    ans = max(ans, i**p)

print(ans)
