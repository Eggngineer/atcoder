
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

k = int(input())
res = ""

for i in range(k):
    res+=chr(ord('A')+i)

print(res)