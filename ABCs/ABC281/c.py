
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,t = map(int,input().split())
a = list(map(int,input().split()))

a_sum = [0]*n
a_sum[0]=a[0]

for i in range(1,n):
    a_sum[i] = a_sum[i-1] + a[i]

fulla = a_sum[~0]

remain = t%fulla
ans = 0
track = 1
if remain <= a_sum[0]:
    ans = remain
else:
    for i in range(1,n):
        if remain <= a_sum[i]:
            ans = remain - a_sum[i-1]
            track = i+1
            break

print(track,ans)