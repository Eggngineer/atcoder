
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for _ in range(m)]

alltime = sum(t)


t = list(zip(t, list(range(n))))

for info in px:
    q, time = info
    info.append(time-t[q-1][0])

for i in range(m):
    print(alltime+px[i][2])
