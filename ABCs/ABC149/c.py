
from math import sqrt
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

x = int(input())


def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
        else:
            return True


while isPrime(x) != True:
    x += 1

print(x)
