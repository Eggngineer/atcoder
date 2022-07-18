import sys
input = sys.stdin.readline


N =int(input())
dig1 =str((N%100)//10)
dig2 =str(N%10)
ret=dig1+dig2
print(ret)
