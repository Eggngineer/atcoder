
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = input().rstrip()
s = s.replace('00','0')
print(len(s))
