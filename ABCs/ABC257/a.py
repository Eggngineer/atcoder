
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, X = map(int,input().split())
dic = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
X = (X-1)//N

print(dic[X])


