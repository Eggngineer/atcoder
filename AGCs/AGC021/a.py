
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

p = 0
while 10**(p+1) <= n:
    p += 1

if p == 0:
    ans = n
else:
    if n % (10**p) == 10**p-1:
        ans = n // (10**p)
    else:
        ans = n // (10**p)-1
    ans += p*9

print(ans)
