from curses.ascii import isupper
import sys
input = sys.stdin.readline

def is_upsorted(query):
    for i in range(len(query)-1):
        if query[i]<=query[i+1]:
            continue
        else:
            return False
            break
    else:
        return True

N, K = map(int,input().rstrip('\n').split())
a = list(map(int, input().rstrip('\n').split()))

b = [ sorted(a[i::K]) for i in range(K)]

for i in range(len(b)-1):
    if b[i][0]<=b[i+1][0]:
        continue

c = []
for i in range(N):
    c.append(b[i%K][i//K])

print("Yes" if is_upsorted(c) else "No")

