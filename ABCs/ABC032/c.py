"""
Shactory method 
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
    print(N)
else:
    r = 0
    tmp = 1
    leng = 0
    maxlen = 0

    for l in range(N):

        while r < N:
            if tmp*S[r] <= K:
                tmp *= S[r]
                r += 1
            else:
                break
        maxlen = max(maxlen, r-l)

        if l == r:
            r += 1
        else:
            tmp //= S[l]

    print(maxlen)
