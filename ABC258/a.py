
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

K = int(input())
hh, mm = 21, 0

h, m = divmod(K, 60)

hh += h
mm += m

print(str(hh)+":"+str(mm).zfill(2))
