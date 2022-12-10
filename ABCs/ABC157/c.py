
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
sc = [list(map(int,input().split())) for _ in range(m)]

result = -1
for i in range(0,1000):
    num = str(i)
    if len(num) != n:
        continue
    else:
        isOK= True

        for j in range(len(sc)):
            si,ci = sc[j]
            if int(num[si-1]) == ci:
                isOK = True
            else:
                isOK = False
                break
        if isOK and (i >= (10**(n-1)) or i ==0):
            result = i
            break

print(result)
