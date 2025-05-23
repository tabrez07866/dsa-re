#sum of 1 to n

# def fun(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     fun(sum+i,i+1,n)

# fun(0,1,5)

#muliply 1 to n

# def fun(mul,i,n):
#     if i>n:
#         print(mul)
#         return
#     fun(mul*i,i+1,n)

# fun(1,1,5)

def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)
a=fun(5)
print(a)

