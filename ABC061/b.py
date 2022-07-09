
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
cities = [0]*n

for _ in range(m):
    c1, c2 = map(int, input().split())
    cities[c1-1] += 1
    cities[c2-1] += 1

for c in cities:
    print(c)
