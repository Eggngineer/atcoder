
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

x1, y1, x2, y2 = map(int, input().split())
xtmo, ytmo = x2-x1, y2-y1
x3, y3 = x2-ytmo, y2+xtmo
x4, y4 = x1-ytmo, y1+xtmo

print(x3, y3, x4, y4)
