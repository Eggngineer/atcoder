
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, l = map(int, input().split())
ss = [input().rstrip() for _ in range(n)]

ss.sort()

ans = ""
for s in ss:
    ans += s

print(ans)
