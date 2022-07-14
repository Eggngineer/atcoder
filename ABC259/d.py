
from math import sqrt
from re import S
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n = int(input())
sx, sy, tx, ty = map(int, input().split())
xyr = [list(map(int, input().split())) for _ in range(n)]

s, t = [sx, sy, 0], [tx, ty, 0]


def norm(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


nmat = [[] for _ in range(n)]
start = -1
goal = -1


for i in range(n):
    if norm(xyr[i], s) == xyr[i][2]:
        start = i
    if norm(xyr[i], t) == xyr[i][2]:
        goal = i

    for j in range(i+1, n):
        if norm(xyr[i], xyr[j]) <= xyr[i][2] + xyr[j][2] and norm(xyr[i], xyr[j]) >= min(xyr[i][2], xyr[j][2]):
            nmat[i].append(j)
            nmat[j].append(i)
    if norm(xyr[i], t) == xyr[2]:
        nmat[i].append(-1)


def search(cir, searching, searched):
    isOK = False
    # print(nmat[cir])
    ret = []
    if goal in nmat[cir]:
        isOK = True
        return isOK, ret
    else:
        if all([p in searching or p in searched for p in nmat[cir]]):
            return isOK, ret
        else:
            for p in nmat[cir]:
                # print(p)
                if p not in searching:
                    ret.append(p)
            # print('>>', ret)
            return isOK, ret


def solve(stt):
    # print(nmat[stt])
    isOK = False
    pt = stt
    searching = []
    searched = []
    searching.append(pt)

    while searching and nmat[pt]:

        isOK, found = search(pt, searching, searched)
        if isOK:
            break
        elif not found:
            searching.remove(pt)
            searched.append(pt)
        searching = found + searching

        # print(searching, searched)
        pt = searching[0]
    if isOK:
        print('Yes')
    else:
        print('No')


solve(start)
