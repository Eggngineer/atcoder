
import sys
from itertools import permutations
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
p = list(map(int,input().split()))

orig = list(range(n+1))

result = []q
if not sorted(p) == p:
    for i in range(n):
        if sorted(p[i:]) == p[i:]:
            for j in range(n):
                if j == i-1:
                    break
                result.append(orig.pop(p[j]))
            result += []

print(result)