
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
sin, cos = math.sin, math.cos
PI = math.pi
a, b, d = map(int, input().split())


def d2r(d):
    return PI*d/180


def rot(x, y, d):
    _x = x * cos(d2r(d)) - y * sin(d2r(d))
    _y = x * sin(d2r(d)) + y * cos(d2r(d))

    return _x, _y


_a, _b = rot(a, b, d)

print(_a, _b)
