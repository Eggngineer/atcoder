"""
ABC192-C "Multiplication 3"
PANASONIC2020-C "Sqrt Inequality"
JOI 3 Spring "JOI Poster"
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


a,b,c = map(int,input().split())
if c**b>a:
    print("Yes")
else:
    print("No")