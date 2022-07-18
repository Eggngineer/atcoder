import sys
input = sys.stdin.readline

def inRange(num):
    return sMin <= num and num <= sMax

X,A,D,N = map(int,input().rstrip('\n').split())

sMin, sMax = min(A, A+(N-1)*D),max(A, A+(N-1)*D)

if D != 0:
    mod = X % D
else:
    mod = 0


if inRange(X):
    if D != 0:   
        ret = min (abs(A%D-mod), abs(D)-abs(A%D-mod))    
        print(ret)
    else:
        print(abs(X-A))

else:
    print(min(abs(X-sMin),abs(X-sMax)))
    
