
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

for i in range(1, N+1):
    q = int(i*1.08)
    if q == N:
        print(i)
        break
else:
    print(':(')
