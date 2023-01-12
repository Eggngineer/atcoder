
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
x = sorted(list(map(int,input().split())))

d = []
for i in range(m-1):
    d.append(abs(x[i]-x[i+1]))

d.sort()

ans = sum(d[:max(0,m-n)])

print(ans)
