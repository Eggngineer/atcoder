
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
p = list(map(int, input().split()))

min = p[0]

count = 0
for num in p:
    if num <= min:
        min = num
        count += 1

print(count)
