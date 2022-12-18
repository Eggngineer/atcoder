
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
s = [list(input().rstrip()) for _  in range(n)]

sindex = [set([i for i , x in enumerate(skill) if x == "o"]) for skill in s]
ac = set(range(m))


res = 0
for i in range(n):
    for j in range(i+1,n):
        if sindex[i] | sindex[j] == ac:
            res+=1

print(res)