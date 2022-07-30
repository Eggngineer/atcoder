
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

h, w = map(int, input().split())
mineMap = [list(input().rstrip()) for _ in range(h)]
dx = dy = list(range(-1, 2))
field = [[0]*w for _ in range(h)]
for y in range(h):
    for x in range(w):
        for i in dx:
            for j in dy:
                if mineMap[y][x] != "#":
                    if 0 <= x+i < w and 0 <= y+j < h:
                        if mineMap[y+j][x+i] == "#":
                            field[y][x] += 1
                else:
                    field[y][x] = "#"

for line in field:
    print(*line, sep="")
