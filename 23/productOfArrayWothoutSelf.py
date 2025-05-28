nums=[1,2,3,4]

def PrdoctOfArray(nums):
    n=len(nums)
    prefix=[1]*n
    postfix=[1]*n
    res=[1]*n

    prefix[0]=1
    for i in range(1,n):
        prefix[i]=prefix[i-1]*nums[i-1]

    postfix[n-1]=1
    for i in range(n-2,-1,-1):
        postfix[i]=postfix[i+1]*nums[i+1]

    for i in range(n):
        res[i]=prefix[i]*postfix[i]
    return res

res=PrdoctOfArray(nums)
print(res)            
