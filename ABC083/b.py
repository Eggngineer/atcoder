
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def sum_digits(i):
    ret = 0
    while i > 0:
        ret += i % 10
        i //= 10
    return ret


n, a, b = map(int, input().split())

ans = 0

for i in range(n+1):
    sum = sum_digits(i)
    if a <= sum and sum <= b:
        ans += i

print(ans)
