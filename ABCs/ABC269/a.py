
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a,b,c,d  = map(int,input().split())
ans = (a+b)*(c-d)

print(ans)
print("Takahashi")