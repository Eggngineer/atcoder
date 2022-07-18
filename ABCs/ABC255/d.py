import sys
input = sys.stdin.readline

N, Q = map(int,input().rstrip('\n').split())

A = list(map(int, input().rstrip('\n').split()))
X = [int(input().rstrip('\n')) for _ in range(Q)]

ret = 0
for x in X:
    for a in A:
        ret += abs(a-x)
    print(ret)
    ret=0
