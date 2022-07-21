
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

score = [tuple([i+1, b[i], a[i]]) for i in range(n)]

score.sort(key=lambda x: x[0], reverse=False)
score.sort(key=lambda x: x[2], reverse=True)

ans = []

for _ in range(x):
    st = score.pop(0)
    ans.append(st[0])


score.sort(key=lambda x: x[0], reverse=False)
score.sort(key=lambda x: x[1], reverse=True)


for _ in range(y):
    st = score.pop(0)
    ans.append(st[0])


score.sort(key=lambda x: x[0], reverse=False)
score.sort(key=lambda x: x[1]+x[2], reverse=True)


for _ in range(z):
    st = score.pop(0)
    ans.append(st[0])


ans.sort()

for a in ans:
    print(a)
