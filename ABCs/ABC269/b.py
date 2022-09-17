
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

ground=["."]*10
flag=False


S = [list(map(str, input().rstrip())) for _ in range(10)]
ab,cd = [0]*2,[0]*2

for i, line in enumerate(S):
    if line != ground and not flag:
        ab[0]=i+1
        cd=[line.index("#")+1,10-line[-1::-1].index("#")]
        flag=True
    if line != ground and flag:
        ab[1]=i+1

print(*ab)
print(*cd)    
