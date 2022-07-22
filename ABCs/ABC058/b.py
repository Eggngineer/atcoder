
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

o = list(input().rstrip())
e = list(input().rstrip())

if len(o) > len(e):
    e.append("")
while o or e:
    print(o.pop(0), end="")
    print(e.pop(0), end="")

print()
