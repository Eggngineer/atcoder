
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dist(v1):
    return abs(v1[0])+abs(v1[1])

def is_horizontal(v1,v2):
    if dot(v1,v2) == 0 and dist(v1) == dist(v2):
        return True
    else:
        return False

def dot(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]

def is_square(four_points):
    four_points.sort()
    v1 = [four_points[0][0]-four_points[3][0],four_points[0][1]-four_points[3][1]]
    v2 = [four_points[1][0]-four_points[2][0],four_points[1][1]-four_points[2][1]]

    return is_horizontal(v1,v2)

s = [list(input().rstrip()) for _ in range(9)]
count = 0

pone = []


for i in range(9):
    for j in range(9):
        if s[i][j] == "#":
            pone.append((i,j))

for i in range(len(pone)):
    for j in range(i+1,len(pone)):
        for k in range(j+1,len(pone)):
            for l in range(k+1,len(pone)):
                if is_square([pone[i],pone[j],pone[k],pone[l]]):
                    print(pone[i],pone[j],pone[k],pone[l])
                    count+=1
    

print(count)


