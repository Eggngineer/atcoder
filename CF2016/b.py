
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, A, B = map(int, input().split())
S = list(input().rstrip())

rem = {'a': 'Yes', 'b': 'Yes', 'c': 'No'}

DL = A+B
for s in S:
    if s == 'c':
        print('No')
        continue

    if DL > 0:
        if s == 'a':
            print('Yes')
            DL -= 1
        if s == 'b':
            if B > 0:
                print('Yes')
                DL -= 1
                B -= 1
            else:
                print('No')
    else:
        print('No')
