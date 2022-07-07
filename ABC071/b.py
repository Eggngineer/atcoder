
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(set(input().rstrip()))
for i in range(26):
    al = chr(ord('a')+i)
    if al not in s:
        print(al)
        break
else:
    print('None')
