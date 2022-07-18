
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]

isCalled = [[False]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            isCalled[i][j] = True
ans = 'No'
if isCalled[0][0] and isCalled[1][1] and isCalled[2][2]:
    ans = 'Yes'
elif isCalled[2][0] and isCalled[1][1] and isCalled[0][2]:
    ans = 'Yes'
elif isCalled[0][0] and isCalled[0][1] and isCalled[0][2]:
    ans = 'Yes'
elif isCalled[1][0] and isCalled[1][1] and isCalled[1][2]:
    ans = 'Yes'
elif isCalled[2][0] and isCalled[2][1] and isCalled[2][2]:
    ans = 'Yes'
elif isCalled[0][0] and isCalled[1][0] and isCalled[2][0]:
    ans = 'Yes'
elif isCalled[0][1] and isCalled[1][1] and isCalled[2][1]:
    ans = 'Yes'
elif isCalled[0][2] and isCalled[1][2] and isCalled[2][2]:
    ans = 'Yes'

print(ans)
