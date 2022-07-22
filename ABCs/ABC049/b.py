
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

h, w = map(int, input().split())
c = [list(input().rstrip()) for _ in range(h)]

for line in c:
    print(*line, sep="")
    print(*line, sep="")
