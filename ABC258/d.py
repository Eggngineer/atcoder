
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, X = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
A = []
B = []
idx = range(N)

for i in range(N):
    A.append(AB[i][0])
    B.append(AB[i][1])

minN = 1e32
all = 0
minB = 1e9
for j in range(N):
    if X < 0:
        break
    X -= 1
    minB = min(minB, B[j])
    all += A[j]+B[j]
    minN = min(minN, all+minB*X)
    # print(minN)sss

print(int(minN))
