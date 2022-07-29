
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int, input().split()))

alen = sum(a)
tmp = a[0]
ans = alen

for i in range(1, n):
    score = abs(alen-2*tmp)
    ans = min(ans, score)
    tmp += a[i]

print(ans)
