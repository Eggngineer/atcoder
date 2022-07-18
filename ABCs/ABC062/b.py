
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

h, w = map(int, input().split())
a = ['#'+input().rstrip()+'#' for _ in range(h)]

bar = '#'*(w+2)

print(bar)
for row in a:
    print(row)
print(bar)
