
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
A = [list(map(int, list(input().rstrip()))) for _ in range(N)]


takahashi = ""
maxtakahashi = 0
nmax = 0
indmax = []


for i in range(N):
    for j in range(N):
        x, y = i, j
        # print("(", x, y, ")")
        for k in range(-1, 2):
            for l in range(-1, 2):
                if k == 0 and l == 0:
                    continue
                for _ in range(N):
                    takahashi += str(A[x][y])
                    boxmax = 0
                    x += k
                    y += l
                    x, y = x % N, y % N
                if int(takahashi) > int(maxtakahashi):
                    maxtakahashi = takahashi

                takahashi = ""


print(maxtakahashi)
