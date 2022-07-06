
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a, b, c = map(int, input().split())
count = 0
if a == b and b == c and a % 2 == 0:
    print(-1)
else:
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        count += 1
        _a, _b, _c = a/1, b/1, c/1
        a = (_b+_c)/2
        b = (_c+_a)/2
        c = (_a+_b)/2

    print(count)
