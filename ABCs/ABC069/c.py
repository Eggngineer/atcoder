
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n = int(input())
a = list(map(int,input().split()))

ret = "Yes"
odd, two, four = [0]*3

for ai in a:
    if ai % 2 == 0:
        if ai % 4 == 0:
            four += 1
        else:
            two += 1
    else:
        odd += 1

if not (odd <= four or (odd == four + 1 and two == 0) ) :
    ret = "No"

print(ret)