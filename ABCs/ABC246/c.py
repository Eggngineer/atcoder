n,k,x=map(int,input().split())
a=list(map(int,input().split()))

sum=0
print(a)

for one in reversed(a):
    num = one//x
    if k<num:num=k
    sum+=one-num*x
    k-=num
    if k==0:
        break

print(k)
print(sum)
