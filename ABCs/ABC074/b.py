
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
K = int(input())
x = list(map(int, input().split()))

ans = 0

for z in x:
    ans += 2 * min(z, abs(K-z))

print(ans)
