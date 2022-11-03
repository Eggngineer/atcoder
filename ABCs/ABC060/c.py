
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, t = map(int, input().split())
times = list(map(int, input().split()))

result = 0
out = [0, t]

for ti in times[1:]:
    if out[0] < ti <= out[1]:
        out[1] = max(ti + t, out[1])
    else:
        result += out[1] - out[0]
        out = [ti, ti + t]
else:
    result += out[1] - out[0]

print(result)