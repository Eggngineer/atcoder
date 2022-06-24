"""
ABC168-C "Colon"
ABC197-C "Oposite"
ABC144=D "Water Bottle"
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from math import cos,sin,tan,atan,pi,sqrt

def norm(p1,p2):
    return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def rad2deg(rad):
    return rad*180.0/pi

def deg2rad(deg):
    return deg*pi/180

T = int(input())
L, X, Y = map(int,input().split())
r = L/2
Cy, Cz = 0, r
# Y-=L/2
Q = int(input())
B = [int(input()) for _ in range(Q)]

w= 360 / T
for time in B:
    theta = w*(-time) - 90
    px,py,pz = 0,Cy+r*cos(deg2rad(theta)),Cz + r*sin(deg2rad(theta))
    px,py,pz = round(px,7),round(py,7),round(pz,7)
    # print(px,py,pz)
    dist = norm([X,Y],[px,py])
    # print(dist,pz)
    ans = abs(atan(pz/dist))
    print(rad2deg(ans))

