
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def horizontal(v1,v2):
    mult = v1[0]*v2[0]+v1[1]*v2[1]
    if mult == 0:
        return True
    else:
        return False

def vect_add(v1,v2):
    return [v1[0]+v2[0], v1[1]+v2[1]]

def linear(a,v):
    return [a*v[0],a*v[1]]

def mh_dist(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

here = [0,0]

d = [[-1,0],[1,0],[0,-1],[0,1]]
n, x, y =map(int,input().split())
a = list(map(int,input().split()))
goal = [x,y]

a1 = a.pop(0)        
here = vect_add(here,linear(a1,[1,0]))
print(*here)
past_vec = [1,0]
for ai in a:
    min_vec = [1,0]
    for dk in d:
        print(mh_dist(goal, vect_add(here,linear(ai,dk))),mh_dist(goal,vect_add(here,linear(ai,min_vec))))
        if mh_dist(goal, vect_add(here,linear(ai,dk))) <= mh_dist(goal,vect_add(here,linear(ai,min_vec))) and horizontal(past_vec,dk):
            min_vec = dk
    here = vect_add(here,linear(ai,min_vec))
    past_vec = min_vec
    print(*here)
    
if here == goal:
    print('Yes')
else:
    print('No')