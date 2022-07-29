
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

abc = list(map(int, input().split()))
a, b, c = sorted(abc)

ans = 0

ans += c-b
a += (c-b)
b += (c-b)

if (c-a) % 2 == 1:
    ans += 1
    b, c = b+1, c+1

ans += (c-a) // 2

print(ans)
