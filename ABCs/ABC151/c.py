from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
ps = [list(map(str, input().split())) for _ in range(m)]

# ps.sort(key=lambda x: x[0])

score = defaultdict(int)

ans = 0
cnt = 0
for i in range(m):
    # print(score)
    if ps[i][1] == 'AC' and not score[ps[i][0]] == -1:
        ans += score[ps[i][0]]
        score[ps[i][0]] = -1
        cnt += 1
    elif not score[ps[i][0]] == -1:
        score[ps[i][0]] += 1

print(cnt, ans)
