
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n, x, y = map(int, input().split())

red, blue, level = 1, 0, n

while level > 1:
    blue += red * x
    red += blue
    blue *= y
    level -= 1

print(blue)
