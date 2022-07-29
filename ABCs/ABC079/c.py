
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

ans = None
strops = ["-", "+"]
ops = [-1, 1]
a, b, c, d = map(int, list(input().rstrip()))
bcd = [b, c, d]

for i in range(2**3):
    tmp = a
    aop = []
    for j in range(3):
        op = i >> j & 1
        aop.append(op)
        tmp += ops[op]*bcd[j]
    if tmp == 7:
        ans = aop
        break

print(str(a)+strops[ans[0]]+str(b)+strops[ans[1]] +
      str(c)+strops[ans[2]]+str(d)+"=7")
