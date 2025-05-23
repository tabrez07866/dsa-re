num=12121
n=num
res=0;
while(n>0):
    lg=n%10
    res=res*10+lg
    n=n//10
print(res==num)    