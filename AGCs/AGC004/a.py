
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

abc = list(map(int, input().split()))
a, b, c = sorted(abc)

if a % 2 and b % 2 and c % 2:
    ans = a*b
else:
    ans = 0

print(ans)
