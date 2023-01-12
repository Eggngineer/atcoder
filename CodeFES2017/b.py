
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
d = list(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))

have = {}
need = {}

for di in d:
    if di not in have:
        have[di] = 0
    have[di] += 1
for ti in t:
    if ti not in need:
        need[ti] = 0
    need[ti] += 1

ans = "YES"
for key in need.keys():
    if key not in have or have[key] < need[key]:
        ans = "NO"
        break

print(ans)