
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

h,m = map(int,input().split())

def is_Bad(h,m):
    h1 = h // 10
    h2 = h % 10
    m1 = m // 10
    m2 = m % 10
    if (0 <= h1*10 + m1 <= 23) and (0 <= h2*10 + m2 <= 59):
        return True
    else:
        return False

if is_Bad(h=h,m=m):
    print(h,m)
else:
    while not is_Bad(h,m):
        m+=1
        if m==60:
            h+=1
            m=0
        if h==24:
            h=0
    print(h,m)