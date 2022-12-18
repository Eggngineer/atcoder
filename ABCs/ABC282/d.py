
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    u,v = u-1,v-1
    g[u].append(v)
    g[v].append(u)

ans = n * (n - 1) // 2 - m
visited = [0] * n

for s in range(n):
    if visited[s] == 0:
        visited[s] = 1
    else:
        continue

    cnt = [0,1,0]
    togo = [s]
    while togo:
        now = togo.pop()
        for t in g[now]:
            if visited[t]:
                if visited[t] == visited[now]:
                    print(0)
                    exit()
            else:
                togo.append(t)
                visited[t] = -visited[now]
                cnt[visited[t]]+=1
    ans -= cnt[1]*(cnt[1]- 1) // 2
    ans -= cnt[-1]*(cnt[-1] -1) // 2
print(ans)