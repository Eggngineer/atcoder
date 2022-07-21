
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input().rstrip())

ct = {}
for c in s:
    if not c in ct:
        ct[c] = 0
    ct[c] += 1

keys, values = list(ct.keys()), list(ct.values())

for i in range(len(keys)):
    if values[i] == 1:
        print(keys[i])
        break
else:
    print(-1)
