
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())


a, b = 1, 2

ans = 0

if n == 0:
    print(b)
elif n == 1:
    print(a)
else:
    for _ in range(n-2+1):
        a, b = a+b, a

    print(a)
