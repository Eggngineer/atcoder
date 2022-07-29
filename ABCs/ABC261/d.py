
from operator import mul
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n, m = map(int, input().split())
x = list(map(int, input().split()))
cy = [list(map(int, input().split())) for _ in range(m)]

rui = [0]*(n+1)

s = 0
allsum = sum(x)
for i in range(m):
    s += cy[i][1]
    allsum += cy[i][1]
    rui[cy[i][0]] = s

ans = allsum

for b in cy:
    k, v = b
    mask = ([1]*k+[0])*(n//k)
    mask = mask[:n]
    base = sum(list(map(mul, mask, x)))
    base += rui[k]*int(n//(k+1)) + rui[int(n % (k+1))]
    ans = max(base, ans)
    print(base, ans)

print(ans)
