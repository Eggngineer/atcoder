from calendar import c
import sys
input = sys.stdin.readline

h1,h2,h3,w1,w2,w3 = map(int,input().rstrip('\n').split()) 


m11 = min(w1,h1) - 2 # >=1
m12 = min(w2 - 2, h1-m11-1)
m21 = min(w1-m11-1,h2 - 2 ) 
m22 = min(w2-m12 - 1 ,h2-m21-1)

res = m11*m12*m21*m22
print(res)