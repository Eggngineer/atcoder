
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
ansl = []
sum = 0
while n > 0:
    xdig = min(4,n)
    sum += xdig
    ansl.append(xdig)
    n -= xdig
m = sum *2

ans = 0
for i in reversed(range(len(ansl))):
    ans *= 10
    ans += ansl[i]

print(m)
print(ans)