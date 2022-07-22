
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
repo = []
for i in range(n):
    line = list(map(str, input().rsplit()))
    line[1] = int(line[1])
    repo.append(line+[i+1])

s, p = 0, 1

repo.sort(key=lambda x: (x[0], -x[1]))

for i in range(n):
    print(repo[i][2])
