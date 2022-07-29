
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

d = {}


n = int(input())
s = [input().rstrip() for _ in range(n)]

for i in range(n):
    word = s[i]
    if word not in d:
        print(word)
        d[word] = 1
    else:
        print(word+'('+str(d[word])+')')
        d[word] += 1
