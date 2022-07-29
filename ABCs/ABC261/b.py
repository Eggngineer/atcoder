
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = [list(input().rstrip()) for _ in range(n)]

aT = [list(x) for x in zip(*a)]


for i in range(n):
    for j in range(n):
        if aT[i][j] == 'W':
            aT[i][j] = 'L'
        elif aT[i][j] == 'L':
            aT[i][j] = 'W'

print('correct' if a == aT else 'incorrect')
