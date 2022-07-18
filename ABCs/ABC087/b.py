
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
for i in range(min(x//500, a)+1):
    y = x-i*500
    for j in range(min(y//100, b)+1):
        z = y - j*100
        if z//50 <= c:
            ans += 1
print(ans)
