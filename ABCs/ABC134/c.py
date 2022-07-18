
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a = [int(input()) for _ in range(n)]

asorted = sorted(list(set(a)), reverse=True)

a1 = asorted[0]
acheck = [False]*n
for i in range(n):
    if a[i] == a1:
        acheck[i] = True
acs = sum(acheck)
if len(asorted) == 1:
    a2 = asorted[0]
else:
    a2 = asorted[1]

for i in range(n):
    if a[i] == a1 and acs == 1:
        print(a2)
    else:
        print(a1)
