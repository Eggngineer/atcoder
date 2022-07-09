
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a, b = map(int, input().split())


def isPN(n):
    if int(n//100 % 10*100+n//1000 % 10*10+n//10000 % 10) == n % 1000:
        return True
    else:
        return False


ans = 0
for i in range(a, b+1):
    if isPN(i):
        ans += 1

print(ans)
