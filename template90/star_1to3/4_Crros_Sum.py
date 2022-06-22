"""
ABC129:D Lamp
ARC077:D 11
"""
import sys
input = sys.stdin.readline

def T(mat):
    return list(zip(*mat))

H, W = map(int,input().rstrip('\n').split())
A = [list(map(int, input().rstrip('\n').split())) for _ in range(H)]
A_t= T(A)

ah = [sum(A[i]) for i in range(H)]
aw = [sum(A_t[j]) for j in range(W)]

for x in range(H):
    for y in range(W):
        print(ah[x]+aw[y]-A[x][y],end=" ")
    print("")
