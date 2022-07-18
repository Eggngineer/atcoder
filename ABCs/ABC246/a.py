import numpy as np

c1=list(map(int,input().split()))
c2=list(map(int,input().split()))
c3=list(map(int,input().split()))

c1=np.asarray(c1)
c2=np.asarray(c2)
c3=np.asarray(c3)

if np.all((c1==c2))==False:
    