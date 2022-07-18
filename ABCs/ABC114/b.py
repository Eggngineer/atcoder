
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = input().rstrip()
l = len(s)

amin = 753

for i in range(l-3+1):
    n = int(s[i:i+3])
    amin = min(amin, abs(n-753))

print(amin)
