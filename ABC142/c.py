
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int, input().split()))

idx = list(range(n))

x = list(sorted(zip(a, idx)))

for st in x:
    print(st[1]+1, end=" ")
print("")
