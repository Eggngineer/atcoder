
import sys
from turtle import right
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, l, r = map(int, input().split())
ai = list(map(int, input().split()))

r_isgot = False
l_isgot = False

x, y = 0, 0

lsum_tmp = 0
lsum_real = 0
for i, a in enumerate(ai):
    if lsum_tmp+l < lsum_real+a:
        x = i+1
    lsum_real += a
    lsum_tmp += l

ai[:x] = [l]*x
print(ai)

rsum_tmp = 0
rsum_real = 0
for i, a in enumerate(reversed(ai)):
    print(rsum_tmp, rsum_real)
    if rsum_tmp+r < rsum_real+a:
        y = i+1
    rsum_real += a
    rsum_tmp += r
print(y)
