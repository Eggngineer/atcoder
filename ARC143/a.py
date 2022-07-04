
from collections import abc
from logging.config import stopListening
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

ABC = list(map(int,input().split()))
ABC = sorted(ABC)

eps = min(ABC[2] - ABC[1], ABC[0])

ABC[0] = eps
ABC[2] -= eps

if ABC[1] != ABC[2]:
    print(-1)
else:
    print(eps+ABC[2])
