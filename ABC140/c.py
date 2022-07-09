
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
b = list(map(int, input().split()))

b = [b[0]]+b + [b[-1]]

sum = 0
for i in range(n):
    sum += min(b[i], b[i+1])

print(sum)
