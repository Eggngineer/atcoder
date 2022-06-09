import sys
readline = sys.stdin.readline

n, k = map(int, readline().split())
a = list(map(int, readline().split()))

for i in range(k):
    a[i::k] = sorted(a[i::k])

print("Yes" if sorted(a) == a else "No")