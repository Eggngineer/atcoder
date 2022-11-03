
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,k = map(int,input().split())

w = 0

for i in range(1,n+1):
    x = i
    wi = 1/n
    while x < k:
        wi/=2
        x*=2
    w+=wi

print("{:.10f}".format(w))