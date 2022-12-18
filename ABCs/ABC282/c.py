
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
s = input().rstrip()

sdx = [i for i , x in enumerate(list(s)) if x == '"']
idx = []

for i in range(0,len(sdx),2):
    idx.append([sdx[i],sdx[i+1]])

num,proc=0,0
while num < n:
    ch = s[num]
    if ch ==',':
        ch = '.'

    if proc < len(idx) and  idx[proc][0] < num and num <  idx[proc][1]:
        if ch =='.':
            ch = ','
    if proc < len(idx) and num == idx[proc][1]+1:
        proc += 1
    print(ch,end="")
    num+= 1

print('\n')