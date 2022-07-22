import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(map(int, list(input().rstrip())))
k = int(input())


i = 0
while i < len(s) and i < k:
    if s[i] != 1:
        print(s[i])
        break
    i += 1

if i == len(s) or i == k:
    print(1)
