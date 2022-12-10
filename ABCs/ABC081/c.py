
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, k = map(int, input().split())
a = list(map(int, input().split()))

l = [0]*n

for ai in a:
    l[ai-1] += 1
l.sort()

kinds = len(set(a))
sum = 0
for i in range(n):
    if kinds <= k:
        break
    if l[i] != 0:
        sum += l[i]
        kinds -= 1


print(sum)
