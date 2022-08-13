
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]


inv = []

b0 = [b[i][0] for i in range(h2)]

for i in range(h1):
    if a[i][0] not in b0:
        inv.append(i)


for num in reversed(inv):
    h1 -= 1
    a.pop(num)

inv = []


if a:
    for i in range(w1):
        if a[0][i] not in b[0]:
            inv.append(i)/search

    for num in reversed(inv):
        for i in range(h1):
            a[i] = a[i][:num]+a[i][num+1:]

    ans = (a == b)
else:
    ans = False

print('Yes' if ans else 'No')
