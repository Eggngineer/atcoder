
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a, b = map(int, input().split())

ans = 0

for i in range(10000+1):
    ia, ib = i*0.08//1, i*0.1//1
    if ia == a//1 and ib == b//1:
        ans = i
        break
else:
    ans = -1

print(ans)
