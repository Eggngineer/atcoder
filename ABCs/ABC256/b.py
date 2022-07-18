import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
A = list(map(int, input().rstrip('\n').split()))
P=0
block = [0]*8

for a in A:
    block[0]=1
    block[a:] = block[:-a]
    block[:a] = [0]*a
    P+=sum(block[4:])
    block[4:] = [0]*4
    

print(P)