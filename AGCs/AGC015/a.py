
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,a,b = map(int,input().split())
if n>=2 and b>=a:
    result = max(n-2,0)*(b-a)+1
elif n==1 and b==a:
    result = 1
else:
    result = 0

print(result)