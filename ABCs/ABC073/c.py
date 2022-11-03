
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
d = {}
for _ in range(n):
    num = int(input())
    if num not in d:
        d[num]=1
    else:
        d[num]^=1

result = sum(d.values())

print(result)