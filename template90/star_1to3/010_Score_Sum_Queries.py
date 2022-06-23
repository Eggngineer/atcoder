import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

CLASS,SCORE = 0,1

N = int(input())
CP = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

S_1 = [0]*(N+1)
S_2 = [0]*(N+1)

S_1_sum=0
S_2_sum=0

for i,student in enumerate(CP):
    i
    if student[CLASS] == 1:
        S_1_sum+=student[SCORE] 
    else:
        S_2_sum+=student[SCORE] 

    S_1[i+1] = S_1_sum
    S_2[i+1] = S_2_sum

for pair in LR:
    left,right = pair[0]-1, pair[1]
    one = S_1[right]-S_1[left]
    second = S_2[right]-S_2[left]
    print(one,second)
