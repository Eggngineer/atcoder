
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

q = [0]

idx = 0
print(0)
while n >= 2**idx:
    for p in q:
        num = p+2**idx
        if num | n == n and num > q[-1]:
            q.append(num)
            print(num)
    idx+=1