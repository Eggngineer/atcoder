
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int,input().split()))
d = {}

min2,min3=50,50

for ai in a:
    i, j=0,0
    if ai%2==0:

        while ai>=2**(i+1) and ai%(2**(i+1))==0:
            i+=1
    if ai%3==0:
        while ai >=3**(j+1) and ai%(3**(j+1))==0:
            j+=1

    min2 = min(i,min2)
    min3 = min(j,min3)
    d[ai]=(None,None,i,j)

result = 0
for i in range(n):
    result += d[a[i]][2]+d[a[i]][3]-min2-min3
    a[i] = a[i]//(2**(d[a[i]][2]-min2))//(3**(d[a[i]][3]-min3))

if not len(set(a))==1:
    print(-1)
else:
    print(result)