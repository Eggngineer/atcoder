
from math import factorial
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

base = 10**9+7
n = int(input())

print(factorial(n) % base)
