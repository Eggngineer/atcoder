import sys
readline = sys.stdin.readline

N = int(input())
count = 0

for i in range(1,N+1):
    k = i
    d = 2
    while(d**2<=k):
        while(k%(d**2)==0):
            k/=(d**2)
        d+=1
    d = 1
    while(k*d**2<=N):
        count += 1
        d += 1
        

print(count)
        