
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def manhattan(v1: list, v2: list):
    return abs(v1[0]-v2[0])+abs(v1[1]-v2[1])


n = int(input())
txy = [list(map(int, input().split())) for _ in range(n)]

now = 0
here = [0]*2

is_able = 'Yes'

for t, x, y in txy:
    cord = [x, y]
    dist = manhattan(here, cord)
    if dist <= t-now and (dist - (t-now)) % 2 == 0:
        now = t
        here = cord
    else:
        is_able = 'No'
        break

print(is_able)