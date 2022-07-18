
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a = int(input())
b = int(input())

if a > b:
    print('GREATER')
elif a < b:
    print('LESS')
else:
    print('EQUAL')
