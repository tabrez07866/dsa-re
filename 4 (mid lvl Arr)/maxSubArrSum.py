nums=[-2,1,-3,4,-1,2,1,-5,4]
maxi=float("-inf")
n=len(nums)
'''
for i in range(0,n):
    total=0
    for j in range(i,n):
        total=total+nums[j]
        maxi=max(total,maxi)
print(maxi)    
'''


#Kadane's theorem
total=0
for i in range(0,n):
    total=total+nums[i]
    maxi=max(total,maxi)
    if total<0:
        total=0
print(maxi)            