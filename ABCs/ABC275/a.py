
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
h = list(map(int,input().split()))

asch = sorted(range(len(h)), key=lambda x:h[x], reverse=True)

print(asch[0]+1)