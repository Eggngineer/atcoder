
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input().rstrip())
db = []

w = ""
for c in s:
    w += c
    if not db:
        db.append(w)
        w = ""
    elif db[-1] != w:
        db.append(w)
        w = ""

print(len(db))
