
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

ans = 10**12-1

for i in range(1, int(n**(1/2))+1):
    if n % i == 0:
        ans = min(ans, n//1 // i-1+i-1)


print(ans)
