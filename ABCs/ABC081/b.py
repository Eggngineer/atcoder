
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    n = 0
    while a[i] % 2 == 0:
        a[i] //= 2
        n += 1
    a[i] = n

ans = min(a)

print(ans)
