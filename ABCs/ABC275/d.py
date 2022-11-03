
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

d = {0:1}

def f(n):
    if n in d:
        return d[n]
    else:
        d[n] = f(n//2)+f(n//3)
    return d[n]

n = int(input())
print(f(n))