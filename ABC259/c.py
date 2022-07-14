
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = list(input().rstrip())
t = list(input().rstrip())


s_ct, t_ct = [], []

n = s[0]
ct = 1
for i in range(1, len(s)):
    if s[i] != n:
        s_ct.append([n, ct])
        n = s[i]
        ct = 1
    else:
        ct += 1
s_ct.append([n, ct])

n = t[0]
ct = 1
for i in range(1, len(t)):
    if t[i] != n:
        t_ct.append([n, ct])
        n = t[i]
        ct = 1
    else:
        ct += 1
t_ct.append([n, ct])

if len(s_ct) != len(t_ct) or set(s) != set(t):
    ans = 'No'
else:
    for i in range(len(s_ct)):
        if s_ct[i][1] > t_ct[i][1]:
            ans = 'No'
            break
        elif s_ct[i][1] == t_ct[i][1]:
            continue
        elif s_ct[i][1] == 1:
            ans = 'No'
        else:
            ans = 'Yes'
print(ans)
