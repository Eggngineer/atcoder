
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
menu = [a, b, c, d, e]
mod = [dish % 10 for dish in menu]
mod, menu = list(zip(*sorted(zip(mod, menu))))

ans = 0
control = True

for dish in menu:
    if control and dish % 10 != 0:
        ans += dish % 10-10
        control = False
    ans += -(-dish//10)*10
print(ans)
