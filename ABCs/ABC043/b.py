
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


s = list(input().rstrip())

stdout = []

for si in s:
    if si == "0":
        stdout.append(0)
    elif si == "1":
        stdout.append(1)
    else:
        if stdout:
            stdout.pop(-1)

print("".join(map(str,stdout)))