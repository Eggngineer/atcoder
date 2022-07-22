
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a, b, k = map(int, input().split())

ans = []

for i in range(a, min(a+k, b)):
    ans.append(i)
for i in range(max(a, b-k+1), b+1):
    ans.append(i)

ans = set(ans)

for a in ans:
    print(a)
