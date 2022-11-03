
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

h,w = map(int,input().split())
s = [list(input().rstrip()) for _ in range(h)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

result = 'Yes'

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            for d in range(4):
                idx,jdy = i+dx[d],j + dy[d]
                if idx in range(h) and jdy in range(w):
                    if s[idx][jdy] == "#":
                        break
            else:
                result = 'No'
                break

print(result)
