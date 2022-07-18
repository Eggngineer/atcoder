
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,a,b = map(int,input().split())
l = list(map(int,input().split()))


l.sort()
ave = sum(l)/n

dif = 0

for el in l:
    if ave>el:
        dif += ave-el
    else:
        break

if l[-1] - l[0] < a+b:
    ans = l[0]
else:
    ans = int(ave - (b-a)/n * (dif//a))

print(ans)