
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
s = list(input().rstrip())

ans = 0
score = 0
for lit in s:
    if lit == "I":
        score += 1
    else:
        score -= 1
    ans = max(ans, score)

print(ans)
