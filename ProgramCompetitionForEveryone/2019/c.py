
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

k,a,b = map(int,input().split())

biscuit = 0

if b-a <= 2:
    ans = k+1
else:
    ans = a + (k-(a-1))//2 * (b-a) + (k-(a-1))%2

print(ans)
