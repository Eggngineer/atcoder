import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
X = list(map(int, input().split()))
X = sorted(X)

xmean = round(sum(X)/N)

ans = 0

for x in X:
    ans += (x-xmean)**2

print(ans)
