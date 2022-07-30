
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


d = defaultdict(int)

n = int(input())
a = list(map(int, input().split()))
rabbits = set(a)

for i in range(n):
    d[i+1] = a[i]

ans = 0

for rabbit in list(range(1, n+1)):
    if rabbit in rabbits:
        rabbits.remove(rabbit)
        if d[rabbit] in rabbits:
            if d[d[rabbit]] == rabbit:
                rabbits.remove(d[rabbit])
                ans += 1
    if not rabbits:
        break

print(ans)
