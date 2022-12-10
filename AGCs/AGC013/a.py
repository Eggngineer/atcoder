
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n = int(input())
a = list(map(int,input().split()))

ans = 0
i = 0
while i < n:
    ans += 1
    j = i + 1
    while j < n and a[i] == a[j]:
        j += 1
    if j < n and a[i] <= a[j]:
        while j < n and a[j-1] <= a[j]:
            j += 1
    elif j < n and a[i] >= a[j]:
        while j < n and a[j-1] >= a[j]:
            j += 1
    i = j

print(ans)

