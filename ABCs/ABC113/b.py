
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
h = list(zip(h, list(range(n))))

h.sort()

mindif = 10**5
minidx = 0

for (height, idx) in h:
    htmp = t-height*0.006
    dif = abs(htmp-a)
    if dif < mindif:
        minidx = idx+1
        mindif = dif

print(minidx)
