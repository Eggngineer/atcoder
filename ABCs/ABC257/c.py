import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

CHILD,ADULT = 0,1

N = int(input())
S = list(map(int,input().rstrip('\n')))
num_adult = sum(S)
W = list(map(int, input().split()))

W_sorted, S_sorted_byW = list(zip(*(sorted(zip(W,S)))))

result = num_adult
max_result = 0
back_person = 0

for idx in range(len(S_sorted_byW)):
    person = W_sorted[idx]
    CorA = S_sorted_byW[idx]
    if person != back_person:
        max_result = max(result,max_result)

    if CorA == CHILD:
        result+=1
    elif CorA == ADULT:
        result-=1

    # print(max_result)
    back_person = person

max_result = max(result,max_result)
print(max_result)

