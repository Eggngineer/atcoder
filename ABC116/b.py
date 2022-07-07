
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = int(input())
his = []
count = 1
while s not in his:
    count += 1
    his.append(s)
    if s % 2 == 0:
        s = s/2
    else:
        s = 3*s+1

print(count)
