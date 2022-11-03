
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

c = [list(map(int,input().split())) for _ in range(3)]

allsum = 0 
tr = 0
for cs in c:
    allsum += sum(cs)

for i in range(3):
    tr += c[i][i]

result = 'No'

if tr != 0:
    if allsum / tr ==3:
        result = 'Yes'
else:
    if allsum == tr:
        result = 'Yes'
print(result)