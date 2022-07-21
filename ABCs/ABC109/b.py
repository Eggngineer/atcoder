
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
words = []

for _ in range(n):
    w = words.append(input().rstrip())

tail = words[0][-1]

wset = list(set(words))

for i in range(1, n):
    if len(wset) != len(words):
        print('No')
        break
    head = words[i][0]
    if head == tail:
        tail = words[i][-1]
    else:
        print('No')
        break
else:
    print('Yes')
