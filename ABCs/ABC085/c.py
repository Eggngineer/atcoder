
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, y = map(int,input().split())

ret = [-1]*3

for i in range(n+1):
    for j in range(0, n-i+1):
        if i * 10000 + j * 5000 + (n-j-i) * 1000 == y:
            ret = [i,j,n-j-i]
            break

print(*ret)